#Arguements: iPlot, region, isCategorized, directory, blind, yLog, rebinning

plotList='tmass tmassBins chi2 ProbChi2 ProbChi2zoom JetPt JetEta JetPhi MET METphi HT NJets NJetsAK8 NBJets NBJetsL JetPtAK8 JetEtaAK8 JetPhiAK8 JetSDMassAK8 JetSDMassCorrAK8 JetTau21AK8 lepPt lepEta lepPhi HybridJet1Pt HybridJet2Pt HybridJet3Pt HybridJet4Pt'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot PS False kinematicsPS_051720 False False 
    python plotTemplates.py $iPlot PS False kinematicsPS_051720 False True  
    python plotTemplates.py $iPlot CR False kinematicsCR_051720 False False
    python plotTemplates.py $iPlot CR False kinematicsCR_051720 False True
    python plotTemplates.py $iPlot SR False kinematicsSR_051720 True False
    python plotTemplates.py $iPlot SR False kinematicsSR_051720 True True
done

plotList='fittedLepPt fittedLepEta fittedLepPhi fittedLepMass fittedMETPt fittedMETPhi fittedMETEta fittedMETMass fittedJetEta fittedJetPt fittedJetPhi fittedJetMass'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot CR False kinematicsCR_051720 False False
    python plotTemplates.py $iPlot CR False kinematicsCR_051720 False True
    python plotTemplates.py $iPlot SR False kinematicsSR_051720 True False
    python plotTemplates.py $iPlot SR False kinematicsSR_051720 True True
done

plotList='tmass'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot SR True templatesSR_051720 True False 0p3
    python plotTemplates.py $iPlot SR True templatesSR_051720 True True 0p3
done

plotList='tmassBins'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot SR True templatesSR_051720 True False 1p1
    python plotTemplates.py $iPlot SR True templatesSR_051720 True True 1p1
done

plotList='HT'
for iPlot in $plotList; do
    echo $iPlot
    python plotTemplates.py $iPlot AltSR True templatesAltSR_051720 True False 0p3
    python plotTemplates.py $iPlot AltSR True templatesAltSR_051720 True True 0p3
done
 