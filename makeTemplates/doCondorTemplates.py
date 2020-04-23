import os,sys,datetime,itertools

thisDir = os.getcwd()
if thisDir[-13:] == 'makeTemplates': runDir = thisDir[:-13]
else: runDir = thisDir
if os.getcwd()[-17:] == 'singleLepAnalyzer': os.chdir(os.getcwd()+'/makeTemplates/')
outputDir = thisDir+'/'
region='PS' #PS,CR, SR
categorize=0 #1==categorize into W or not, haven't taught analyze.py about that yet

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix = 'templates'+region
if not categorize: pfix='kinematics'+region
pfix+='_Take3'

iPlotList = [#distribution name as defined in "doHists.py"

	'tmass',
	'chi2',
	'ProbChi2',
	'ProbChi2zoom',

	'JetPt', 
	'JetEta',
	'JetPhi',

	'MET',   
	'METphi',

	'HT',
	'NJets', 
	'NJetsAK8',
	'NBJets',
	'NBJetsL',

	'JetPtAK8',
	'JetEtaAK8',
	'JetPhiAK8',

	'lepPt', 
	'lepEta',
	'lepPhi',
	
	'HybridJet1Pt',
	'HybridJet2Pt',
	'HybridJet3Pt',
	'HybridJet4Pt',

	]

isEMlist = ['E','M']

taglist = ['all']
if categorize: taglist=['0W','1pW'] ## analyze.py doesn't understand this yet

outDir = outputDir+pfix+'/'
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.system('cp ../analyze.py doHists.py ../utils.py ../weights.py ../samples.py doCondorTemplates.py doCondorTemplates.sh '+outDir+'/')
os.chdir(outDir)

catlist = list(itertools.product(isEMlist,taglist))

count=0
for iplot in iPlotList:
	for cat in list(itertools.product(isEMlist,taglist)):
		catDir = cat[0]+'_'+cat[1]	
		outDir = outputDir+pfix+'/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		os.chdir(outDir)			

		dict={'rundir':runDir, 'dir':'.','iPlot':iplot,'region':region,'isCategorized':categorize,
			  'isEM':cat[0],'tag':cat[1]}
		print dict
		jdf=open('condor.job','w')
		jdf.write(
			"""use_x509userproxy = true
universe = vanilla
Executable = %(rundir)s/makeTemplates/doCondorTemplates.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = ../analyze.py, ../samples.py, ../utils.py, ../weights.py, ../doHists.py
Output = condor_%(iPlot)s.out
Error = condor_%(iPlot)s.err
Log = condor_%(iPlot)s.log
Notification = Never
Arguments = %(dir)s %(iPlot)s %(region)s %(isCategorized)s %(isEM)s %(tag)s

Queue 1"""%dict)
		jdf.close()
		
		os.system('condor_submit condor.job')
		os.chdir('..')
		count+=1

print "Total jobs submitted:", count
                  
