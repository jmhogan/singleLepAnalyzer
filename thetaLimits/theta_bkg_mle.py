import os,sys,pickle
from operator import itemgetter,attrgetter

category = str(sys.argv[2])

input = '/uscms_data/d3/jmanagan/CMSSW_10_2_10/src/tptp_2016/makeTemplates/templatesSRCR_June2020TT/templates_DnnTprime_TTM1400_bW0p5_tZ0p25_tH0p25_35p867fb_BKGNORM_rebinned_stat0p3.root'

if 'FullMu' in category: input = '/uscms_data/d3/bluetke/MVATraining/CMSSW_10_2_16/src/singleLepAnalyzer/makeTemplates/templatesCR_June2020TT/templates_HTNtag_TTM1400_bW0p5_tZ0p25_tH0p25_41p53fb_rebinned_stat0p3.root'

rFileName = input.split('/')[-1][:-5]


print 'File:',rFileName,', category:',category
                                                                                                                                          
def get_model():
    if 'All' in category: model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('sig')==0 and s.count('Jeff')==0 and s.count('Jmis')==0))
    elif 'CR' in category: model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s: s.count('sig')==0 and s.count('Jeff')==0 and s.count('Jmis')==0 and s.count('tagged')==0 and s.count('notV')==0))
    
    model.fill_histogram_zerobins()
    model.set_signal_process_groups({'':[]})
    
    procs = model.processes
    obsvs = model.observables.keys()
    
    for obs in obsvs:
        if 'isE' in obs:
            try: model.add_lognormal_uncertainty('elIdSys', math.log(1.027), '*', obs) #Arguments: uncertainty name, magnitude of uncertainty, which processes it applies to, which channel or observable
            except: pass
            #try: model.add_lognormal_uncertainty('elIsoSys', math.log(1.01), '*', obs) #iso + reco
            #except: pass
            #try: model.add_lognormal_uncertainty('elRecoSys', math.log(1.01), '*', obs) #iso + reco
            #except: pass
        elif 'isM' in obs:
            try: model.add_lognormal_uncertainty('muIdSys', math.log(1.027), '*', obs)
            except: pass
            #try: model.add_lognormal_uncertainty('muIsoSys', math.log(1.01), '*', obs) #iso + tracking
            #except: pass
            #try: model.add_lognormal_uncertainty('muRecoSys', math.log(1.01), '*', obs) #iso + tracking
            #except: pass
        
                         
    try: model.add_lognormal_uncertainty('lumiSys', math.log(1.025), '*', '*')
    except: pass

    if 'FullMu' not in category:
        try: model.add_lognormal_uncertainty('QCDrate', math.log(1.25), 'qcd', '*')
        except: pass
        try: model.add_lognormal_uncertainty('EWKrate', math.log(1.25), 'ewk', '*')
        except: pass
        try: model.add_lognormal_uncertainty('TOPrate', math.log(1.35), 'top', '*')
        except: pass

    flatpars = {'mean': 0.0, 
                'range': [float('-inf'), float('inf')], 
                'typ': 'gauss', 
                'width': float('inf')}

    if 'Flat' in category:
        model.distribution.distributions.update({'Teff': flatpars})
        model.distribution.distributions.update({'Tmis': flatpars})
        model.distribution.distributions.update({'Heff': flatpars})
        model.distribution.distributions.update({'Hmis': flatpars})
        model.distribution.distributions.update({'Zeff': flatpars})
        model.distribution.distributions.update({'Zmis': flatpars})
        model.distribution.distributions.update({'Weff': flatpars})
        model.distribution.distributions.update({'Wmis': flatpars})
        model.distribution.distributions.update({'Beff': flatpars})
        model.distribution.distributions.update({'Bmis': flatpars})


    return model


##################################################################################################################

model = get_model()

model_summary(model)

options = Options()
if 'robust' in category:
    options.set('minimizer', 'strategy', 'robust')
    options.set('minimizer', 'minuit_tolerance_factor', '100')

#parVals = mle(model, input='data', n=1, with_error=True, chi2=True, ks = True, with_covariance=True, options=options)
parVals = mle(model, input='toys-asimov:0', n=1, with_error=True, with_covariance=True, options=options)

parameter_values = {}
for syst in parVals[''].keys():
    if syst=='__nll' or syst=='__cov': continue
    if 'chi2' in syst: print 'Found chi2:',syst,', values:',parVals[''][syst][0],', length=',len(parVals[''][syst])
    elif 'ks' in syst: print 'Found K-S:',syst,', values:',parVals[''][syst][0],', length=',len(parVals[''][syst])
    else:
        print syst,"=",parVals[''][syst][0][0],"+/-",parVals[''][syst][0][1]
        parameter_values[syst] = parVals[''][syst][0][0]

pickle.dump(parVals,open(rFileName+'_'+category+'.p','wb'))

histos = evaluate_prediction(model, parameter_values, include_signal=False)
write_histograms_to_rootfile(histos, 'histos-mle_'+category+'.root')

from numpy import linalg
import numpy as np

theta_res = parVals['']
param_list = []
for k, res in theta_res.iteritems():
    #print k,',',res
    if any(k == i for i in ['__nll','__cov','__chi2','__ks']): continue
    err_sq = res[0][1]*res[0][1]
    param_list.append((k, err_sq))

cov_matrix = theta_res['__cov'][0]
ind_dict = {}
for i in xrange(cov_matrix.shape[0]):
    for ii in xrange(cov_matrix.shape[1]):
        entry = cov_matrix[i,ii]
        for proc, val in param_list:
            if abs(val-entry) < 1e-6:
                if i != ii:
                    self.message("WARNING row and column index don't match")
                ind_dict[i] = proc
            if i not in ind_dict.keys():
                ind_dict[i] = 'beta_signal'

cov_matrix = np.matrix(cov_matrix)
diag_matrix = np.matrix(np.sqrt(np.diag(np.diag(cov_matrix))))
#try:
inv_matrix = diag_matrix.I
corr_matrix = inv_matrix * cov_matrix * inv_matrix

corr_hist = ROOT.TH2D("correlation_matrix","",len(param_list),0,len(param_list),len(param_list),0,len(param_list))
cov_hist = ROOT.TH2D("covariance_matrix","",len(param_list),0,len(param_list),len(param_list),0,len(param_list))
    
for i in xrange(corr_matrix.shape[0]):
    if i not in ind_dict.keys(): continue
    corr_hist.GetXaxis().SetBinLabel(i+1, ind_dict.get(i,'unknown'))
    corr_hist.GetYaxis().SetBinLabel(i+1, ind_dict.get(i,'unknown'))
    cov_hist.GetXaxis().SetBinLabel(i+1, ind_dict.get(i,'unknown'))
    cov_hist.GetYaxis().SetBinLabel(i+1, ind_dict.get(i,'unknown'))
    corr_hist.SetLabelSize(0.03,'x')
    cov_hist.SetLabelSize(0.03,'x')
    corr_hist.GetZaxis().SetRangeUser(-1,1)
    for ii in xrange(corr_matrix.shape[1]):
        entry_corr = corr_matrix[i,ii]
        entry_cov = cov_matrix[i,ii]
        corr_hist.Fill(i,ii,entry_corr)
        cov_hist.Fill(i,ii,entry_cov)

matrices = ROOT.TFile('mle_covcorr_'+category+'.root','RECREATE')
cov_hist.Write()
corr_hist.Write()
matrices.Close()

report.write_html('htmlout_'+rFileName+'_'+category)

