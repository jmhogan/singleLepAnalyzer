#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,getopt
from ROOT import TH1D,gROOT,TFile,TTree
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from numpy import linspace
from weights import *
from analyze import *
from samples import *
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
step1Dir = 'root://cmseos.fnal.gov//store/user/jmanagan/NanoAODv6_1lep2018_040920_step1haddsHTSF'

iPlot = 'lepPt' #minMlb' #choose a discriminant from plotList below!
if len(sys.argv)>2: iPlot=sys.argv[2]
region = 'PS'
if len(sys.argv)>3: region=sys.argv[3]
isCategorized = False
if len(sys.argv)>4: isCategorized=int(sys.argv[4])
doJetRwt= 1
doTopRwt= 0
doAllSys= True
cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templatesTest'+region
if not isCategorized: pfix='kinematicsTEST'+region
#pfix+=iPlot
#pfix+='_'+datestr#+'_'+timestr

"""
Note: 
--Each process in step1 (or step2) directories should have the root files hadded! 
--The code will look for <step1Dir>/<process>_hadd.root for nominal trees.
The uncertainty shape shifted files will be taken from <step1Dir>/../<shape>/<process>_hadd.root,
where <shape> is for example "JECUp". hadder.py can be used to prepare input files this way! 
--Each process given in the lists below must have a definition in "samples.py"
--Check the set of cuts in "analyze.py"
"""

bkgList = [

	'DYMG200','DYMG400','DYMG600','DYMG800','DYMG1200','DYMG2500',
	'WJetsMG200','WJetsMG400','WJetsMG600','WJetsMG800','WJetsMG1200','WJetsMG2500',
	'TTJetsHad','TTJetsSemiLep','TTJets2L2nu',
#	'TTJetsHad0','TTJetsHad700','TTJetsHad1000','TTJetsSemiLep0','TTJetsSemiLep700','TTJetsSemiLep1000','TTJets2L2nu0','TTJets2L2nu700','TTJets2L2nu1000',
#	'TTJetsPH700mtt','TTJetsPH1000mtt','Ts','Tbs',
        'Ts','Tt','Tbt','TtW','TbtW',#'TTWl','TTZl','TTHB','TTHnoB','TTWq',
#	'WW','WZ','ZZ',
	'QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000'
	]

dataList = [
	'DataEABCDEF',
	'DataMABCDEF',
	]

whichSignal = 'TT' #HTB, TT, BB, or X53X53
massList = range(1000,1800+1,100)
sigList = [whichSignal+'M'+str(mass) for mass in massList]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in massList for chiral in ['left','right']]
if whichSignal=='TT': decays = ['']#'BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays

cutList = {'lepPtCut':55,'metCut':50,'nAK8Cut':3,'dnnCut':0.50,'HTCut':510} ## also requires mass reco worked
if 'CR' in region :cutList = {'lepPtCut':55,'metCut':50,'nAK8Cut':3,'dnnCut':0.50,'HTCut':510} 
if 'PS' in region :cutList = {'lepPtCut':55,'metCut':50,'nAK8Cut':0,'dnnCut':0.0,'HTCut':510} ## most basic

if len(sys.argv)>5: isEMlist=[str(sys.argv[5])]
else: isEMlist = ['E']
if len(sys.argv)>6: taglist=[str(sys.argv[6])]
else: 
	taglist = ['all']
	if isCategorized and whichSignal == 'TT': taglist=['taggedbWbW']#,'taggedtHbW','taggedtHtH','taggedtZbW','taggedtZtH','taggedtZtZ','taggedtZHtZH','notV']
	elif isCategorized and whichSignal == 'BB': taglist=['taggedtWtW','taggedbHtW','taggedbHbH','taggedbZtW','taggedbZbH','taggedbZbZ','notV']

#bigbins = [0,50,100,150,200,250,300,350,400,450,500,600,700,800,1000,1200,1500]
bigbins = [0,50,100,125,150,175,200,225,250,275,300,325,350,375,400,450,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,5000]

nbins = 51
xmax = 800
if isCategorized and 'SR' in region: 
	nbins = 101
	xmax = 1000

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
        'lepPt' :('Lepton_pt',linspace(0, 1000, 51).tolist(),';Lepton p_{T} [GeV];'),
        'lepEta':('Lepton_eta',linspace(-4, 4, 41).tolist(),';Lepton #eta;'),
	'lepPhi':('Lepton_phi',linspace(-3.2,3.2,65).tolist(),';#phi(l)'),

        'JetEta':('Jet_eta',linspace(-4, 4, 41).tolist(),';AK4 Jet #eta;'),
        'JetPt' :('Jet_pt',linspace(0, 1500, 51).tolist(),';jet p_{T} [GeV];'),
        'JetPhi':('Jet_phi',linspace(-3.2,3.2,65).tolist(),';AK4 Jet #phi'),

        'tmass':('tMass',linspace(50,2450,51).tolist(),';M(t) [GeV]'),
        'chi2':('chi2',linspace(0,1000,51).tolist(),';chi^{2}'),
        'ProbChi2':('exp(-chi2/2)',linspace(0,1,51).tolist(),';Prob chi^{2}'),
        'ProbChi2zoom':('exp(-chi2/2)',linspace(0,0.05,51).tolist(),';Prob chi^{2}'),

        'MET':('MET_pt',linspace(0, 1500, 51).tolist(),';#slash{E}_{T} [GeV];'),
        'METphi':('MET_phi',linspace(-3.2, 3.2, 65).tolist(),';#phi(#slash{E}_{T});'),

        'HT':('AK4HT',linspace(0, 5000, nbins).tolist(),';H_{T} (GeV);'),
        'NJets':('NJets',linspace(0, 15, 16).tolist(),';jet multiplicity;'),
        'NBJets':('NJetsDeepCSVmed',linspace(0, 10, 11).tolist(),';b-tagged jet multiplicity;'),
        'NBJetsL':('NJetsDeepCSVloose',linspace(0, 10, 11).tolist(),';loose b-tagged jet multiplicity;'),
        'NJetsAK8':('NFatJets',linspace(0, 10, 11).tolist(),';AK8 jet multiplicity;'),

        'JetPtAK8':('FatJet_pt',linspace(0, 1500, 51).tolist(),';AK8 jet p_{T} [GeV];'),
        'JetEtaAK8':('FatJet_eta',linspace(-4,4, 41).tolist(),';AK8 jet #eta;'),
        'JetPhiAK8':('FatJet_phi',linspace(-3.2,3.2,65).tolist(),';AK8 Jet #phi'),

        'HybridJet1Pt':('HybridJet_pt[0]',linspace(0, 1500, 51).tolist(),';1st jet p_{T} [GeV];'),
        'HybridJet2Pt':('HybridJet_pt[1]',linspace(0, 1500, 51).tolist(),';2nd jet p_{T} [GeV];'),
        'HybridJet3Pt':('HybridJet_pt[2]',linspace(0, 1500, 51).tolist(),';3rd jet p_{T} [GeV];'),
        'HybridJet4Pt':('HybridJet_pt[3]',linspace(0, 1500, 51).tolist(),';4th jet p_{T} [GeV];'),



}
print "PLOTTING:",iPlot
print "         LJMET Variable:",plotList[iPlot][0]
print "         X-AXIS TITLE  :",plotList[iPlot][2]
print "         BINNING USED  :",plotList[iPlot][1]

shapesFiles = []#['jec','jer','btag','ltag']
tTreeData = {}
tTreeSig = {}
tTreeBkg = {}

catList = list(itertools.product(isEMlist,taglist))
print 'Cat list:',catList
nCats  = len(catList)
catInd = 1
for cat in catList:
	print '==================== Category:',cat,'======================'
 	catDir = cat[0]+'_'+cat[1]
 	datahists = {}
 	bkghists  = {}
 	sighists  = {}
 	if len(sys.argv)>1:
		outDir=sys.argv[1]
		sys.path.append(outDir)
 	else: 
		outDir = os.getcwd()
		outDir+='/'+pfix
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
 	category = {'isEM':cat[0],'tag':cat[1]}

	print 'Running analyze'
 	for data in dataList: 
		print '-------------------------'
		tTreeData[data]=readTreeNominal(samples[data],step1Dir) ## located in utils.py
 		datahists.update(analyze(tTreeData,data,cutList,False,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized,whichSignal))
 		if catInd==nCats: 
			print 'deleting',data
			del tTreeData[data]
 	for bkg in bkgList: 
		print '-------------------------'
		tTreeBkg[bkg]=readTreeNominal(samples[bkg],step1Dir)
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					print "        "+syst+ud
					tTreeBkg[bkg+syst+ud]=readTreeShift(samples[bkg],syst.upper()+ud.lower(),step1Dir) ## located in utils.py
 		bkghists.update(analyze(tTreeBkg,bkg,cutList,doAllSys,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized,whichSignal))
 		if catInd==nCats:
			print 'deleting',bkg
			del tTreeBkg[bkg]
			if doAllSys:
				for syst in shapesFiles:
					for ud in ['Up','Down']: del tTreeBkg[bkg+syst+ud]

 	for sig in sigList: 
 	 	for decay in decays: 
			print '-------------------------'
			tTreeSig[sig+decay]=readTreeNominal(samples[sig+decay],step1Dir)
			if doAllSys:
				for syst in shapesFiles:
					for ud in ['Up','Down']:
						print "        "+syst+ud
						tTreeSig[sig+decay+syst+ud]=readTreeShift(samples[sig+decay],syst.upper()+ud.lower(),step1Dir)
 	 		sighists.update(analyze(tTreeSig,sig+decay,cutList,doAllSys,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized,whichSignal))
 	 		if catInd==nCats: 
				print 'deleting',sig+decay
				del tTreeSig[sig+decay]
				if doAllSys:
					for syst in shapesFiles:
						for ud in ['Up','Down']: del tTreeSig[sig+decay+syst+ud]

 	#Negative Bin Correction
	for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])
 	for sig in sighists.keys(): negBinCorrection(sighists[sig])

 	# #OverFlow Correction
 	for data in datahists.keys(): overflow(datahists[data])
 	for bkg in bkghists.keys():   overflow(bkghists[bkg])
 	for sig in sighists.keys():   overflow(sighists[sig])

	
 	pickle.dump(datahists,open(outDir+'/datahists_'+iPlot+'.p','wb'))
	pickle.dump(bkghists,open(outDir+'/bkghists_'+iPlot+'.p','wb'))
	pickle.dump(sighists,open(outDir+'/sighists_'+iPlot+'.p','wb'))
 	catInd+=1

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))
