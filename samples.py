#!/usr/bin/python

samples = {
'DataEABCDEF':'NanoAOD_25Oct_SingleEl',
'DataMABCDEF':'NanoAOD_25Oct_SingleMu',

'TTM900':'TprimeTprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1000':'TprimeTprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1100':'TprimeTprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1200':'TprimeTprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1300':'TprimeTprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1400':'TprimeTprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1500':'TprimeTprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1600':'TprimeTprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1700':'TprimeTprime_M-1700_TuneCP5_PSweights_13TeV-madgraph-pythia8',
'TTM1800':'TprimeTprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8',


'DYMG200':'DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYMG400':'DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYMG600':'DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYMG800':'DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYMG1200':'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYMG2500':'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'WJetsMG200':'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG400':'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG600':'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG800':'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG1200':'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG2500':'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',

#'WW':'WW_TuneCP5_13TeV-pythia8',
#'WZ':'WZ_TuneCP5_13TeV-pythia8',
#'ZZ':'ZZ_TuneCP5_13TeV-pythia8',

#'TTJetsPH':'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',

'TTJetsHad':'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
'TTJetsHad0':'TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Mtt0to700',
'TTJetsHad700':'TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Mtt700to1000',
'TTJetsHad1000':'TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Mtt1000toInf',

'TTJetsSemiLep':'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
'TTJetsSemiLep0':'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_Mtt0to700',
'TTJetsSemiLep700':'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_Mtt700to1000',
'TTJetsSemiLep1000':'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_Mtt1000toInf',

'TTJets2L2nu':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
'TTJets2L2nu0':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_Mtt0to700',
'TTJets2L2nu700':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_Mtt700to1000',
'TTJets2L2nu1000':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_Mtt1000toInf',

#'TTJetsPH700mtt':'TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8',
#'TTJetsPH1000mtt':'TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8',

#'TTZl':'TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
#'TTWl':'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
#'TTHB':'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8',
#'TTHnoB':'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8',
#'TTWH':'TTWH_TuneCP5_13TeV-madgraph-pythia8',

'Ts':'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8',
#'Ts':'ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia',
#'Tbs':'ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia',
'Tbt':'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
'Tt':'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
'TbtW':'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
'TtW':'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',

#'TTWq':'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',

'QCDht200':'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht300':'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht500':'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht700':'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht1000':'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht1500':'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCDht2000':'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
}



