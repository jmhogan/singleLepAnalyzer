#Arguements: iPlot, region, isCategorized, directory, blind, yLog, rebinning

#plotList='probSumDecay probSumFour probb probh probj probt probw probz dnnLargest nB nH nT nW nZ DnnTprime DnnWJets DnnTTbar tmass Wmass tpt Wpt tdrWb Wdrlep isLepW HT ST JetPt MET NJets NBJets iNBDeepJets NJetsAK8 JetPtAK8 lepPt SoftDrop deltaRAK8 minMlj mindeltaR PtRel mindeltaRAK8 PtRelAK8 lepEta lepIso JetEta JetEtaAK8 NTrue minMlb METmod minDPhiMetJet'
#for iPlot in $plotList; do
#    echo $iPlot
#    python plotTemplates.py $iPlot PS False kinematicsPS_May2020TT_May9 False False 
#    python plotTemplates.py $iPlot PS False kinematicsPS_May2020TT_May9 False True  
    #python plotTemplates.py $iPlot CR False kinematicsCR_May2020TT_May9 False False
    #python plotTemplates.py $iPlot CR False kinematicsCR_May2020TT_May9 False True
#done

#plotList='Tp2Mass Tp1Mass Tp2Pt Tp1Pt Tp1Eta Tp2Eta Tp1Phi Tp2Phi Tp1deltaR Tp2deltaR'
plotList='tmass HT'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot TTCR False kinematicsTTCR_May2020TT_May9 False False
    python plotTemplates.py $iPlot TTCR False kinematicsTTCR_May2020TT_May9 False True
    #python plotTemplates.py $iPlot CR False kinematicsCR_May2020TT_May9 False False
    #python plotTemplates.py $iPlot CR False kinematicsCR_May2020TT_May9 False True
    #python plotTemplates.py $iPlot WJCR False kinematicsWJCR_May2020TT_May9 False False
    #python plotTemplates.py $iPlot WJCR False kinematicsWJCR_May2020TT_May9 False True
    #python plotTemplates.py $iPlot SR False kinematicsSR_May2020TT_May9 True False
    #python plotTemplates.py $iPlot SR False kinematicsSR_May2020TT_May9 True True
done

#plotList='ST HT DnnTprime DnnWJets DnnTTbar'
#for iPlot in $plotList; do
#    echo $iPlot
#    #python plotTemplates.py $iPlot TTCR False kinematicsTTCR_May2020TT_May9 False False 
#    #python plotTemplates.py $iPlot TTCR False kinematicsTTCR_May2020TT_May9 False True
#    python plotTemplates.py $iPlot WJCR False kinematicsWJCR_May2020TT_May9 False False 
#    python plotTemplates.py $iPlot WJCR False kinematicsWJCR_May2020TT_May9 False True
#    #python plotTemplates.py $iPlot SR False kinematicsSR_May2020TT_May9 True False
#    #python plotTemplates.py $iPlot SR False kinematicsSR_May2020TT_May9 True True
#done

#plotList='DnnTprime'
#for iPlot in $plotList; do
#    echo $iPlot
#    python plotTemplates.py $iPlot SR True templatesSR_May2020TT_May9 True False 0p3
#    python plotTemplates.py $iPlot SR True templatesSR_May2020TT_May9 True True 0p3
#done



# SPECIAL PS PLOTS
#plotList='DnnTprime DnnWJets DnnTTbar tmass Wmass tpt Wpt tdrWb Wdrlep isLepW HT ST JetPt MET NJets NBJets NJetsAK8 JetPtAK8 lepPt SoftDrop deltaRAK8 minMlj mindeltaR PtRel mindeltaRAK8 PtRelAK8 lepEta lepIso JetEta JetEtaAK8 NTrue minMlb METmod minDPhiMetJet'
#for iPlot in $plotList; do
#    echo $iPlot
#    python plotTemplates.py $iPlot PS False kinematicsPS_July2019_TT_Rerun_Special False False
#    python plotTemplates.py $iPlot PS False kinematicsPS_July2019_TT_Rerun_Special False True
#done
