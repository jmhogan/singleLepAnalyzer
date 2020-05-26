#!/usr/bin/python
from ROOT import TH1D,TTree,TFile
from array import array
from numpy import linspace
from weights import *

"""
--This function will make kinematic plots for a given distribution for electron, muon channels and their combination
--Check the cuts below to make sure those are the desired full set of cuts!
--The applied weights are defined in "weights.py". Also, the additional weights (SFs, 
negative MC weights, ets) applied below should be checked!
"""

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
def analyze(tTree,process,cutList,doAllSys,doJetRwt,iPlot,plotDetails,category,region,isCategorized,whichSig):
	
	plotTreeName=plotDetails[0]
	xbins=array('d', plotDetails[1])
	xAxisLabel=plotDetails[2]	

	# Define categories
	isEM  = category['isEM']
	tag   = category['tag']
	catStr = 'is'+isEM+'_'+tag#+'_'+algo

	# Design the EM cuts for categories
	isEMCut=''
	if isEM=='E': 
		if 'DataM' in process: isEMCut+='isElectron==0 && isMuon==0' # should be empty
		else: isEMCut+='isElectron==1'
	elif isEM=='M': 
		if 'DataE' in process: isEMCut+='isElectron==0 && isMuon==0' # should be empty
		else: isEMCut+='isMuon==1'
	
		
	# Design the tagging cuts for categories
	tagCut = ''	
        if tag == '0W': tagCut = ' && usesWtag == 0'
	elif tag == '1pW': tagCut = ' && usesWtag == 1'

        cut = ''#NJets >= 3'
	
	if region == 'CR': # 'CR' or 'CRinc'  goodHitFit and fails probchi2
		cut += '&& tMass > 0 && probchi2 > -1 && probchi2 < 0.001'
	elif region == 'AltCR':
		cut += '&& NJetsDeepCSVmed == 0 && NJetsDeepCSVloose != 0'
	elif region == 'AltSR': 
		cut += '&& NJetsDeepCSVmed > 1 && AK4HT > 500'
	elif 'SR' in region: # 'SR'  goodHitFit and pass probchi2
		cut += '&& tMass > 0 && probchi2 > 0.001'
	elif 'PS' in region: # 'PS'  
		if region == 'PS0b': cut += '&& NJetsDeepCSVmed == 0'
		elif region == 'PS2b': cut += '&& NJetsDeepCSVmed > 1'

	fullcut = isEMCut+tagCut+cut
		
	# Define weights change to all 1's!!
	TrigEffElUp = '1'
	TrigEffElDn = '1'
	TrigEffMuUp = '1'#'(triggerSF + isMuon*triggerSFUncert)'
	TrigEffMuDn = '1'#'(triggerSF - isMuon*triggerSFUncert)'
	TrigEff = '1'

	jetSFstr='1'
	jetSFstrUp = '1'
	jetSFstrDn = '1'
	if (process!='WJetsMG' and 'WJetsMG' in process):
		jetSFstr = 'HTSF_Pol'
		jetSFstrUp = 'HTSF_PolUp'
		jetSFstrDn = 'HTSF_PolDn'

	weightStr = '1'
	if 'Data' not in process: 
		# replaced isoSF, MuTrkSF with 1
		weightStr          += ' * '+jetSFstr+' * '+TrigEff+' * pileupWeight * '+str(weight[process])+'* (genWeight/abs(genWeight))'
		if 'TTJets' in process:  weightStr += ' * topPtWeight'
 
#		weightTrigEffElUpStr  = weightStr.replace(TrigEff,TrigEffElUp)
#                weightTrigEffElDownStr= weightStr.replace(TrigEff,TrigEffElDn)
#		weightTrigEffMuUpStr  = weightStr.replace(TrigEff,TrigEffMuUp)
#		weightTrigEffMuDownStr= weightStr.replace(TrigEff,TrigEffMuDn)
		weightPileupUpStr   = weightStr.replace('pileupWeight','pileupWeightUp')
		weightPileupDownStr = weightStr.replace('pileupWeight','pileupWeightDn')
#		weightPrefireUpStr   = weightStr.replace('L1NonPrefiringProb_CommonCalc','L1NonPrefiringProbUp_CommonCalc')
#		weightPrefireDownStr = weightStr.replace('L1NonPrefiringProb_CommonCalc','L1NonPrefiringProbDown_CommonCalc')
		weightmuRFcorrdUpStr   = 'LHEScaleWeight[0] * '+weightStr #'renormWeights[5] * '+weightStr
		weightmuRFcorrdDownStr = 'LHEScaleWeight[8] * '+weightStr#'renormWeights[3] * '+weightStr
		weightmuRUpStr      = 'LHEScaleWeight[1] * '+weightStr#'renormWeights[4] * '+weightStr
		weightmuRDownStr    = 'LHEScaleWeight[7] * '+weightStr#'renormWeights[2] * '+weightStr
		weightmuFUpStr      = 'LHEScaleWeight[3] * '+weightStr#'renormWeights[1] * '+weightStr
		weightmuFDownStr    = 'LHEScaleWeight[5] * '+weightStr#'renormWeights[0] * '+weightStr

		weighttopptUpStr    = weightStr.replace('topPtWeight','1')
		weighttopptDownStr  = weightStr #.replace('topPtWeight13TeV','topPtWeight13TeV*topPtWeight13TeV')
#		weightjsfUpStr      = weightStr.replace(jetSFstr,jetSFstrUp)
#		weightjsfDownStr    = weightStr.replace(jetSFstr,jetSFstrDn)

	print "*****"*20
	print "*****"*20
	print "DISTRIBUTION:", iPlot
	print "            -name in ljmet trees:", plotTreeName
	print "            -x-axis label is set to:", xAxisLabel
	print "            -using the binning as:", xbins

	print "/////"*5
	print "PROCESSING: ", process
	print "/////"*5

	print 'plotTreeName: '+plotTreeName
	print 'Flavour: '+isEM+' #tag: '+tag
	print "Weights:",weightStr
	print 'Cuts: '+fullcut

	# Declare histograms --- COMMENTS FOR UNCERTAINTIES NOT BEING RUN YET
	hists = {}
	hists[iPlot+'_'+lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'_'+lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	if doAllSys:
	#	hists[iPlot+'trigeffElUp_'    +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'trigeffElUp_'    +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'trigeffElDown_'  +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'trigeffElDown_'  +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'trigeffMuUp_'    +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'trigeffMuUp_'    +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
         #       hists[iPlot+'trigeffMuDown_'  +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'trigeffMuDown_'  +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'pileupUp_'     +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'pileupUp_'     +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'pileupDown_'   +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'pileupDown_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'prefireUp_'     +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'prefireUp_'     +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'prefireDown_'   +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'prefireDown_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'muRFcorrdUp_'  +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muRFcorrdUp_'  +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'muRFcorrdDown_'+lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muRFcorrdDown_'+lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'topptUp_'      +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'topptUp_'      +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		hists[iPlot+'topptDown_'    +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'topptDown_'    +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'jsfUp_'        +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'jsfUp_'        +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	#	hists[iPlot+'jsfDown_'      +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'jsfDown_'      +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			
		if process+'jerUp' in tTree: 
			hists[iPlot+'jerUp_'   +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'jerUp_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'jerDown_' +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'jerDown_' +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		if process+'jecUp' in tTree:
			hists[iPlot+'jecUp_'   +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'jecUp_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'jecDown_' +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'jecDown_' +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		if process+'btagUp' in tTree: 
			hists[iPlot+'btagUp_'   +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'btagUp_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'btagDown_' +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'btagDown_' +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
		if process+'ltagUp' in tTree:
			hists[iPlot+'ltagUp_'   +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'ltagUp_'   +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'ltagDown_' +lumiStr+'fb_'+catStr+'_'+process]  = TH1D(iPlot+'ltagDown_' +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)

		if isCategorized:
			hists[iPlot+'muRUp_'        +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muRUp_'        +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'muRDown_'      +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muRDown_'      +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'muFUp_'        +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muFUp_'        +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			hists[iPlot+'muFDown_'      +lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'muFDown_'      +lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
			#for i in range(100): hists[iPlot+'pdf'+str(i)+'_'+lumiStr+'fb_'+catStr+'_'+process] = TH1D(iPlot+'pdf'+str(i)+'_'+lumiStr+'fb_'+catStr+'_'+process,xAxisLabel,len(xbins)-1,xbins)
	for key in hists.keys(): hists[key].Sumw2()

	# DRAW histograms
	tTree[process].Draw(plotTreeName+' >> '+iPlot+''+'_'+lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
	print 'Nominal hist integral: ',hists[iPlot+''+'_'+lumiStr+'fb_'+catStr+'_' +process].Integral()
	if doAllSys:
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'trigeffElUp_'    +lumiStr+'fb_'+catStr+'_'+process, weightTrigEffElUpStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'trigeffElDown_'  +lumiStr+'fb_'+catStr+'_'+process, weightTrigEffElDownStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'trigeffMuUp_'    +lumiStr+'fb_'+catStr+'_'+process, weightTrigEffMuUpStr+'*('+fullcut+')', 'GOFF')
 #               tTree[process].Draw(plotTreeName+' >> '+iPlot+'trigeffMuDown_'  +lumiStr+'fb_'+catStr+'_'+process, weightTrigEffMuDownStr+'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'pileupUp_'     +lumiStr+'fb_'+catStr+'_'+process, weightPileupUpStr+'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'pileupDown_'   +lumiStr+'fb_'+catStr+'_'+process, weightPileupDownStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'prefireUp_'     +lumiStr+'fb_'+catStr+'_'+process, weightPrefireUpStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'prefireDown_'   +lumiStr+'fb_'+catStr+'_'+process, weightPrefireDownStr+'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'muRFcorrdUp_'  +lumiStr+'fb_'+catStr+'_'+process, weightmuRFcorrdUpStr  +'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'muRFcorrdDown_'+lumiStr+'fb_'+catStr+'_'+process, weightmuRFcorrdDownStr+'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'topptUp_'      +lumiStr+'fb_'+catStr+'_'+process, weighttopptUpStr+'*('+fullcut+')', 'GOFF')
		tTree[process].Draw(plotTreeName+' >> '+iPlot+'topptDown_'    +lumiStr+'fb_'+catStr+'_'+process, weighttopptDownStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'jsfUp_'        +lumiStr+'fb_'+catStr+'_'+process, weightjsfUpStr+'*('+fullcut+')', 'GOFF')
#		tTree[process].Draw(plotTreeName+' >> '+iPlot+'jsfDown_'      +lumiStr+'fb_'+catStr+'_'+process, weightjsfDownStr+'*('+fullcut+')', 'GOFF')

		if process+'jecUp' in tTree:
			tTree[process+'jecUp'].Draw(plotTreeName   +' >> '+iPlot+'jecUp_'  +lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
			tTree[process+'jecDown'].Draw(plotTreeName +' >> '+iPlot+'jecDown_'+lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
		if process+'jerUp' in tTree:
			tTree[process+'jerUp'].Draw(plotTreeName   +' >> '+iPlot+'jerUp_'  +lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
			tTree[process+'jerDown'].Draw(plotTreeName +' >> '+iPlot+'jerDown_'+lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
		if process+'btagUp' in tTree:
			tTree[process+'btagUp'].Draw(plotTreeName   +' >> '+iPlot+'btagUp_'  +lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
			tTree[process+'btagDown'].Draw(plotTreeName +' >> '+iPlot+'btagDown_'+lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
		if process+'ltagUp' in tTree:
			tTree[process+'ltagUp'].Draw(plotTreeName   +' >> '+iPlot+'ltagUp_'  +lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')
			tTree[process+'ltagDown'].Draw(plotTreeName +' >> '+iPlot+'ltagDown_'+lumiStr+'fb_'+catStr+'_' +process, weightStr+'*('+fullcut+')', 'GOFF')

		if isCategorized:
			tTree[process].Draw(plotTreeName+' >> '+iPlot+'muRUp_'        +lumiStr+'fb_'+catStr+'_'+process, weightmuRUpStr+'*('+fullcut+')', 'GOFF')
			tTree[process].Draw(plotTreeName+' >> '+iPlot+'muRDown_'      +lumiStr+'fb_'+catStr+'_'+process, weightmuRDownStr+'*('+fullcut+')', 'GOFF')
			tTree[process].Draw(plotTreeName+' >> '+iPlot+'muFUp_'        +lumiStr+'fb_'+catStr+'_'+process, weightmuFUpStr+'*('+fullcut+')', 'GOFF')
			tTree[process].Draw(plotTreeName+' >> '+iPlot+'muFDown_'      +lumiStr+'fb_'+catStr+'_'+process, weightmuFDownStr+'*('+fullcut+')', 'GOFF')
			#for i in range(100): tTree[process].Draw(plotTreeName+' >> '+iPlot+'pdf'+str(i)+'_'+lumiStr+'fb_'+catStr+'_'+process, 'pdfWeights['+str(i)+'] * '+weightStr+'*('+fullcut+')', 'GOFF')
	
	for key in hists.keys(): hists[key].SetDirectory(0)	
	return hists
