#!/usr/bin/python

targetlumi = 59690. # 1/pb

genHTweight={}
genHTweight['WJetsMG100'] = 0.998056#https://github.com/jmhogan/GenHTweight/blob/master/WJetsToLNuSFs.txt
genHTweight['WJetsMG200'] = 0.978569
genHTweight['WJetsMG400'] = 0.928054
genHTweight['WJetsMG600'] = 0.856705
genHTweight['WJetsMG800'] = 0.757463
genHTweight['WJetsMG1200']= 0.608292
genHTweight['WJetsMG2500']= 0.454246

genHTweight['DYMG100'] = 1.007516#https://github.com/jmhogan/GenHTweight/blob/master/DYJetsToLLSFs.txt
genHTweight['DYMG200'] = 0.992853
genHTweight['DYMG400'] = 0.974071
genHTweight['DYMG600'] = 0.948367
genHTweight['DYMG800'] = 0.883340
genHTweight['DYMG1200']= 0.749894
genHTweight['DYMG2500']= 0.617254

BR={}
BR['BW'] = 1.0
BR['TZ'] = 0.0
BR['TH'] = 0.0
BR['TTBWBW'] = BR['BW']*BR['BW']
BR['TTTHBW'] = 2*BR['TH']*BR['BW']
BR['TTTZBW'] = 2*BR['TZ']*BR['BW']
BR['TTTZTZ'] = BR['TZ']*BR['TZ']
BR['TTTZTH'] = 2*BR['TZ']*BR['TH']
BR['TTTHTH'] = BR['TH']*BR['TH']

# Number of processed MC events (before selections)
nRun={}
# new counts as of May 1, 2020




nRun['TTJets2L2nu'] = 63603110.0 # from integral 64120000.0, file TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTJetsHad'] = 129964042.0 # from integral 131024000.0, file TTToHadronic_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTJetsSemiLep'] = 297438664.0 # from integral 299859998.0, file TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_1_hadd.root

nRun['TTJets1000'] = 0 #21288395.0 # from integral 22458751.0, file TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg
nRun['TTJets700'] = 0 #38428627.0 #from 39258853, file TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8_hadd.root

nRun['TTJetsHad0'] = 129819080.0*0.8832 #nRun['TTJetsHad']*0.8832   # hadronic*BR(0-700)
nRun['TTJetsHad700'] = nRun['TTJetsHad']*0.0921 + nRun['TTJets700']*0.457 #hadronic*BR(700-1000) + mass700*BR(hadronic)
nRun['TTJetsHad1000'] = nRun['TTJetsHad']*0.02474 + nRun['TTJets1000']*0.457 #hadronic*BR(1000+) + mass1000*BR(hadronic
nRun['TTJetsSemiLep0'] = 297169208.0*0.8832  # semilept*BR(0-700)
nRun['TTJetsSemiLep700'] = 297655604.0*0.0921 + nRun['TTJets700']*0.438 #semilept*BR(700-1000) + mass700*BR(semilept)
nRun['TTJetsSemiLep1000'] = 296113538.0*0.02474 + nRun['TTJets1000']*0.438 #semilept*BR(1000+) + mass1000*BR(semilept)
nRun['TTJets2L2nu0'] = nRun['TTJets2L2nu']*0.8832  #dilepton*BR(0-700)
nRun['TTJets2L2nu700'] = nRun['TTJets2L2nu']*0.0921 + nRun['TTJets700']*0.105 #dilepton*BR(700-1000) + mass700*BR(dilepton)
nRun['TTJets2L2nu1000'] =63629240.0*0.02474 + nRun['TTJets1000']*0.105 #nRun['TTJets2L2nu']*0.02474 + nRun['TTJets1000']*0.105 #dilepton*BR(1000+) + mass1000*BR(dilepton)
nRun['TTJetsPH700mtt'] = nRun['TTJets700'] + nRun['TTJetsHad']*0.0921 + nRun['TTJetsSemiLep']*0.0921 + nRun['TTJets2L2nu']*0.0921 #mass700 + inclusive*BR(700)
nRun['TTJetsPH1000mtt'] = nRun['TTJets1000'] + nRun['TTJetsHad']*0.02474 + nRun['TTJetsSemiLep']*0.02474 + nRun['TTJets2L2nu']*0.02474 #mass1000 + inclusive*BR(1000)

nRun['Ts'] = 12458638.0 # from integral 19965000.0, file ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['Tbs'] = 2952214. # from integral 2953000.0, file ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root
nRun['Tt'] = 144094782.0 # from integral 154307600.0, file ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_1_hadd.root
nRun['Tbt']= 74227130.0 # from integral 79090800.0, file ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_hadd.root
nRun['TtW'] = 9553912.0 # from integral 9598000.0, file ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TbtW'] = 7588180.0 # from integral 7623000.0, file ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_hadd.root

nRun['WJets'] = 6776900. # from 9908534.
nRun['WJetsMG'] = 86731806. 
nRun['WJetsMG100'] = 79356685.
nRun['WJetsMG200'] = 25423155.0 # from integral 25468933.0, file WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG400'] = 5915969.0 # from integral 5932701.0, file WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG600'] = 19699782.0 # from integral 19771294.0, file WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG800'] = 8362227.0 # from integral 8402687.0, file WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG1200'] = 7571583.0 # from integral 7633949.0, file WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG2500'] = 3191612.0 # from integral 3273980.0, file WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root

nRun['WJetsPt100'] = 120124110.*(1.-2.*0.32) #Full =120124110, neg frac 0.32
nRun['WJetsPt250'] = 12022587.*(1.-2.*0.31555) #Full = 12022587, neg frac 0.31555 
nRun['WJetsPt400'] = 1939947.*(1.-2.*0.30952) #Full = 1939947, neg frac 0.30952
nRun['WJetsPt600'] = 1974619.*(1.-2.*0.29876) #Full = 1974619, neg frac 0.29876

nRun['DY'] = 123584520. # from 182359896, this is the ext1 sample
nRun['DYMG'] = 49082157. # from integral 49125561.0, file DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG100'] = 10607207.
nRun['DYMG200'] = 11206441.0 # from integral 11225887.0, file DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG400'] = 9813120.0 # from integral 9840466.0, file DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG600'] = 8828622.0 # from integral 8862104.0, file DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG800'] = 3121975.0 # from integral 3138129.0, file DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG1200']= 531762.0 # from integral 536416.0, file DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG2500']= 415713.0 # from integral 427051.0, file DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8_hadd.root

nRun['WW'] = 7765828.0 # from integral 7765828.0, file WW_TuneCP5_13TeV-pythia8_hadd.root
nRun['WZ'] = 3928630. # from integral 3928630.0, file WZ_TuneCP5_13TeV-pythia8_hadd.root
nRun['ZZ'] = 1925931.0 # from integral 1925931.0, file ZZ_TuneCP5_13TeV-pythia8_hadd.root

nRun['QCDht100'] = 80684349.
nRun['QCDht200'] = 54251666.0 # from integral 54289442.0, file QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht300'] = 54600685.0 # from integral 54661579.0, file QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht500'] = 55056202.0 # from integral 55152960.0, file QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht700'] = 48038740.0 # from integral 48158738.0, file QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht1000'] = 15407797.0 # from integral 15466225.0, file QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht1500'] = 10887751.0 # from integral 10955087.0, file QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['QCDht2000'] = 5414545.0 # from integral 5475677.0, file QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root

nRun['TTW'] = 9384328. # from integral 9425384.0, file ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTZ'] = 8519074. # from integral 8536618.0, file ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTH'] = 9580578. # from integral 9783674.0, file ttH_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTWl'] = 2692366. #from 4919674
nRun['TTZl'] = 5239484.0 # from integral 11092000.0, file TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_hadd.root
nRun['TTHB'] = 7833734.0 # from integral 8000000.0, file ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTHnoB'] = 7814711.0 # from integral 7161154.0, file ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTWq'] = 441560.0 # from integral 811306.0, file TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root

#TprimeTprime files (all should be BWBW)
nRun['TTM900'] = 818732.0*0.333*0.333 # from integral 838000.0, file TprimeTprime_M-900_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1000'] = 802686.0*0.333*0.333 # from integral 832000.0, file TprimeTprime_M-1000_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1100'] = 795116.0*0.333*0.333 # from integral 838000.0, file TprimeTprime_M-1100_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1200'] = 778462.0*0.333*0.333 # from integral 841000.0, file TprimeTprime_M-1200_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1300'] = 760116.0*0.333*0.333 # from integral 850000.0, file TprimeTprime_M-1300_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1400'] = 710902.0*0.333*0.333 # from integral 832000.0, file TprimeTprime_M-1400_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1500'] = 648060.0*0.333*0.333 # from integral 810000.0, file TprimeTprime_M-1500_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1600'] = 622720.0*0.333*0.333 # from integral 850000.0, file TprimeTprime_M-1600_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1700'] = 551326.0*0.333*0.333 # from integral 850000.0, file TprimeTprime_M-1700_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root
nRun['TTM1800'] = 467962.0*0.333*0.333 # from integral 850000.0, file TprimeTprime_M-1800_TuneCP5_PSweights_13TeV-madgraph-pythia8_hadd.root

# Cross sections for MC samples (in pb) -- most unchanged for 2017
xsec={}
xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG100'] = 147.4*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG200'] = 40.99*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG400'] = 5.678*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG600'] = 1.367*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG800'] = 0.6304*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG1200'] = 0.1514*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG2500'] = 0.003565*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['TTJets700']= 831.76*0.9
xsec['TTJets1000']= 831.76*0.25
xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#xsec['TTJetsPH0to700inc'] = 831.76
#xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
#xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsHad']= 831.76*0.457
xsec['TTJetsHad0'] = 831.76*0.8832*0.457  ## BRs from PDG Top Review 2018: 45.7%/43.8%/10.5% 0/1/2 leptons
xsec['TTJetsHad700'] = 831.76*0.0921*0.457
xsec['TTJetsHad1000'] = 831.76*0.02474*0.457
xsec['TTJetsSemiLep']=831.76*0.438
xsec['TTJetsSemiLep0'] = 831.76*0.8832*0.438
xsec['TTJetsSemiLep700'] = 831.76*0.0921*0.438
xsec['TTJetsSemiLep1000'] = 831.76*0.02474*0.438
xsec['TTJets2L2nu'] = 831.76*0.105
xsec['TTJets2L2nu0'] = 831.76*0.8832*0.105
xsec['TTJets2L2nu700'] = 831.76*0.0921*0.105
xsec['TTJets2L2nu1000'] = 831.76*0.02474*0.105
xsec['TTJetsPH700mtt'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000mtt'] = 831.76*0.02474 #(xsec*filtering coeff.)

xsec['TTHB'] = 0.2934
xsec['TTHnoB'] = 0.215

xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WJetsPt100'] = 676.3 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt250'] = 23.94 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt400'] = 3.031 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt600'] = 0.4524 #B2G-17-010 / AN2016_480_v5
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['TTH'] = 0.5269 # from XsecDB, NLO
xsec['TTW'] = 0.4611 # from XsecDB, LO
xsec['TTZ'] = 0.5407 # from XsecDB, LO
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 136.02 # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
xsec['Tbt'] = 80.95 # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
xsec['Ts'] = 10.32*0.333 #(leptonic, top+antitop) https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
xsec['Tbs'] = 3.97*0.333 #(leptonic, antitop)# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
xsec['TtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
xsec['TbtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec

xsec['TTM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

# Calculate lumi normalization weights
weight = {}
for sample in sorted(nRun.keys()):
	if nRun[sample] != 0: 
		weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])

#  LocalWords:  nRun
