import os,sys

filelist = { 
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_BHBH_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_BHTW_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_BZBH_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_BZBZ_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_BZTW_hadd.root':0,
    'BprimeBprime_M-900_TuneCP5_13TeV-madgraph-pythia8_TWTW_hadd.root':0,
    'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root':0,
    'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root':0,
    'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root':0,
    'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root':0,
    'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root':0,
    'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8_hadd.root':0,
    'ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root':0,
    'ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root':0,
    'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':11,
    'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':19,
    'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':2,
    'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':2,
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_1_hadd.root':7,
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_1_hadd.root':7,
    'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000_1_hadd.root':7,
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_1_hadd.root':4,
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_1_hadd.root':4,
    'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000_1_hadd.root':4,
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_1_hadd.root':12,
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_1_hadd.root':13,
    'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000_1_hadd.root':13,
    'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root':0,
    'TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_1_hadd.root':2,
    'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root':0,
    'TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':5,
    'TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8_1_hadd.root':4,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1000_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1100_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1200_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1300_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1400_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1500_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1600_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1700_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_BWBW_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THBW_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_THTH_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZBW_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTH_hadd.root':0,
    'TprimeTprime_M-1800_TuneCP5_13TeV-madgraph-pythia8_TZTZ_hadd.root':0,
    'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root':17,
    'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root':2,
    'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root':16,
    'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root':7,
    'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root':7,
    'WW_TuneCP5_13TeV-pythia8_hadd.root':0,
    'WZ_TuneCP5_13TeV-pythia8_hadd.root':0,
    'ZZ_TuneCP5_13TeV-pythia8_hadd.root':0,
    'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_1_hadd.root':2,
    'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_1_hadd.root':2,
}

from ROOT import TFile, TH1

#for file in filelist:
#    print('-------------------------------------------------------')
#    rfile = TFile.Open('root://cmseos.fnal.gov//store/user/escharni/FWLJMET102X_1lep2017Dnn_Mar2020_step1hadds/'+file)
#    hist = rfile.Get("weightHist")
#    adjusted = hist.GetBinContent(1)
#    integral = hist.GetBinContent(5) + hist.GetBinContent(7)
#    newpdf = hist.GetBinContent(2)
#
#    if 'prime' not in file:
#        print(str(adjusted)+'. # from integral '+str(integral)+', file '+file)
#    else:
#        print(str(newpdf)+'. # from integral '+str(integral)+', file '+file)


for filekey in sorted(filelist.keys()):
    print('-------------------------------------------------------')
    rfile = TFile.Open('root://cmseos.fnal.gov//store/user/escharni/FWLJMET102X_1lep2017Dnn_Mar2020_step1hadds/'+filekey)
    hist = rfile.Get("weightHist")

    if filelist[filekey] > 0:
        print 'Opening ',filelist[filekey],'files:'
        for ifile in range(2,filelist[filekey]+1):
            #print 'file #',ifile
            tempfile = TFile.Open('root://cmseos.fnal.gov//store/user/escharni/FWLJMET102X_1lep2017Dnn_Mar2020_step1hadds/'+filekey.replace('_1_','_'+str(ifile)+'_'))
            temphist = tempfile.Get("weightHist")
            temphist.SetDirectory(0)
            hist.Add(temphist)
            tempfile.Close()

    adjusted = hist.GetBinContent(1)
    integral = hist.GetBinContent(5) + hist.GetBinContent(7)
    newpdf = hist.GetBinContent(2)

    if 'prime' not in filekey:
        print(str(adjusted)+'. # from integral '+str(integral)+', file '+filekey)
    else:
        print(str(newpdf)+'. # from integral '+str(integral)+', file '+filekey)
