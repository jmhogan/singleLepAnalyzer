from ROOT import *
from array import array
from math import *
import os,sys,pickle

gROOT.SetBatch(1)

from tdrStyle import *
setTDRStyle()

post = sys.argv[1]

blind=False
saveKey=''
lumiPlot = '35.9'
lumiStr = '35p867'
spin=''#'right'
discriminant='DnnTprime'
if 'Dnn' in post: discriminant='DnnTprime'
histPrefix=discriminant+'_'+str(lumiStr)+'fb'+spin
stat='0p3'#0.75
isRebinned='_BKGNORM_rebinned'
tempKey='templatesSRCR_TT_mle'
limitDir='/uscms_data/d3/jmanagan/CMSSW_10_2_10/src/tptp_2016/thetaLimits/limitsJune2020/'+tempKey+'/'
cutString=''#SelectionFile'
LH700file='/templates_'+discriminant+'_TTM1400_bW0p5_tZ0p25_tH0p25_'+lumiStr+'fb'+isRebinned+'_stat'+stat+'_'+post+'.p' #

print limitDir+cutString+LH700file

parVals=pickle.load(open(limitDir+cutString+LH700file,'rb'))

nuisNam = []
nuisVal = []
nuisErr = []
for nuis in parVals[''].keys(): #TpTp_M-0800'].keys():
	if nuis=='__cov' or nuis=='__nll' or nuis=='__chi2' or nuis=='__ks': continue
	nuisNam.append(nuis)
	nuisVal.append(parVals[''][nuis][0][0])
	nuisErr.append(parVals[''][nuis][0][1])
	print nuis,"=",parVals[''][nuis][0][0],"+/-",parVals[''][nuis][0][1]


nuisNam = [
	'elIdSys', #'sfel_id',#
	'muIdSys', #'sfmu_id',#
	'elIsoSys', #'sfel_iso',#
	'muIsoSys', #'sfmu_iso',#
	'elRecoSys', #'sfel_gsf',#
	'muRecoSys', #'sfmu_trk',#
	'trigeffEl',
	'trigeffMu',
	'lumiSys', #'luminosity',#
	'pileup',#
	'jec',
	'jer',
	'jsf',
	'ltag',#
	'btag',#
	'muRFcorrdNewTop',
	'muRFcorrdNewEwk',
	'muRFcorrdNewQCD',#
	'TOPrate',
	'EWKrate',
	'QCDrate',
	'Teff',
	'Tmis',
	'Heff',
	'Hmis',
	'Zeff',
	'Zmis',
	'Weff',
	'Wmis',
	'Beff',
	'Bmis',
	'Jeff',
	'Jmis',
	]

nuisNamPlot = [
	'SFs: e',
	'SFs: #mu',
	'Iso: e',
	'Iso: #mu',
	'Reco: e',
	'Reco: #mu',
	'Trigger: e',
	'Trigger: #mu',
	'Lumi',
	'Pileup',
	'JES',
	'JER',
	'HT scaling',
	'B tag: udsg',
	'B tag: bc',
	'ME Shape Top',
	'ME Shape W/Z/VV',
	'ME Shape QCD',
	'ME Rate Top',
	'ME Rate W/Z/VV',
	'ME Rate QCD',
	'Deep T eff',
	'Deep T mis',
	'Deep H eff',
	'Deep H mis',
	'Deep Z eff',
	'Deep Z mis',
	'Deep W eff',
	'Deep W mis',
	'Deep B eff',
	'Deep B mis',
	'Deep J eff',
	'Deep J mis',       
	]

nuisVal = []
nuisErr = []
delNam = []
delPlot = []
nsuccess=0
print 'initial length',len(nuisNam)
for inui in range(len(nuisNam)):
	nuis = nuisNam[inui]
	try:
		nuisVal.append(parVals[''][nuis][0][0])
		nuisErr.append(parVals[''][nuis][0][1])
		nsuccess+=1
	except:
		delNam.append(nuisNam[inui])
		delPlot.append(nuisNamPlot[inui])		 
		print 'removing',nuisNam[inui]

for nui in delNam: nuisNam.remove(nui)
for nui in delPlot: nuisNamPlot.remove(nui)

nNuis = len(nuisNam)
print 'end length',nNuis

g   = TGraphAsymmErrors(nNuis)
g68 = TGraph(2*nNuis+7)
g95 = TGraph(2*nNuis+7)
for i in range(nNuis):
	g.SetPoint(i, nuisVal[i], i+1.5)
	g.SetPointEXlow(i, nuisErr[i])
	g.SetPointEXhigh(i, nuisErr[i])
for a in xrange(0, nNuis+3):
	g68.SetPoint(a, -1, a)
	g95.SetPoint(a, -1.99, a)
	g68.SetPoint(a+1+nNuis+2, 1, nNuis+2-a)
	g95.SetPoint(a+1+nNuis+2, 1.99, nNuis+2-a)

g.SetLineStyle(1)
g.SetLineWidth(1)
g.SetLineColor(1)
g.SetMarkerStyle(21)
g.SetMarkerSize(1.25)
g68.SetFillColor(ROOT.kGreen)
g95.SetFillColor(ROOT.kYellow)

prim_hist = g.GetHistogram() 
ax_Y = prim_hist.GetYaxis()
ax_X = prim_hist.GetXaxis()

g.SetTitle('')
ax_X.SetTitle('post-fit values')
ax_Y.SetTitleSize(0.050)
ax_X.SetTitleSize(0.050)
ax_Y.SetTitleOffset(1.4)
ax_X.SetTitleOffset(1.0)
ax_Y.SetLabelSize(0.05)
ax_Y.SetRangeUser(0, nNuis+2)
ax_X.SetRangeUser(-3.2, 3.2)

ax_Y.Set(nNuis+2, 0, nNuis+2)
ax_Y.SetNdivisions(-414)
for i in range(nNuis):
	ax_Y.SetBinLabel(i+2, nuisNamPlot[i])

c = TCanvas('PostFit', 'PostFit', 1000, 1600)
c.SetTopMargin(0.04)
c.SetRightMargin(0.04)
c.SetBottomMargin(0.10)
c.SetLeftMargin(0.27)
c.SetTickx()
c.SetTicky()
	
#g95.Draw('AF')
g.Draw('AP')
g95.Draw('F')
g68.Draw('F')
g.Draw('P')

g.GetHistogram().Draw('axis,same')
c.Modified()
c.Update()

type = 'SLBO'
if post=='comb': type = 'CombBO'
if 'comb123' in post: type = 'Comb123BO'
if post=='ssdl': type = '2LBO'
if 'asimov' in tempKey: type = 'SLBO_asimov'

c.SaveAs(limitDir+'postFitNuis_'+type+'_'+post+'.root')
c.SaveAs(limitDir+'postFitNuis_'+type+'_'+post+'.pdf')
c.SaveAs(limitDir+'postFitNuis_'+type+'_'+post+'.png')
c.SaveAs(limitDir+'postFitNuis_'+type+'_'+post+'.C')

