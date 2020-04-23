#Arguements: iPlot, region, isCategorized, directory, blind, yLog, rebinning

plotList='tmass chi2 ProbChi2 JetPt JetEta JetPhi MET METphi HT NJets NJetsAK8 JetPtAK8 JetEtaAK8 JetPhiAK8 lepPt lepEta lepPhi HybridJet1Pt HybridJet2Pt HybridJet3Pt HybridJet4Pt'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot PS False kinematicsPS_Take3 False False 
    python plotTemplates.py $iPlot PS False kinematicsPS_Take3 False True  
done

plotList='tmass chi2 ProbChi2 HybridJet1Pt HybridJet2Pt HybridJet3Pt HybridJet4Pt lepPt MET'

for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot CR False kinematicsCR_Take3 False False
    python plotTemplates.py $iPlot CR False kinematicsCR_Take3 False True
    python plotTemplates.py $iPlot SR False kinematicsSR_Take3 True False
    python plotTemplates.py $iPlot SR False kinematicsSR_Take3 True True
done
 