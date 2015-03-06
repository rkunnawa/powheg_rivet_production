# POWHEG + RIVET generator production

This is a setup to generate lhe files using powheg (for what ever PDF and events you want, dijet or Z+Jet ... ) and to run them to through the RIVET analyzer to get the jet invariant cross section spectra. 

GENERATING POWHEG: 
  You need a working setup of POWHEG box installed (or you can source the CMSSW version which is located here: /afs/cern.ch/sw/lcg/external/MCGenerators/powheg-box/r2092/x86_64-slc6-gcc46-opt/bin/) 
  to set up POWHEG follow this twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/GeneratePowheg 
  1) change the powheg.input file to your necessary specifications. 
  2) Setup the powheg submission script powheg.sub and batch submission file, runmany.sh (where you can change the no of jobs to       run in the runmany.sh) its very important to source 
      $ source runmany.sh
  3) This will give you a bunch of lhe files which contans the event information in them. 
  4) if you are using your own setup of powheg then you have to set the cmssw environment variable and make sure that libraries      point to the correct locations, like what i have in setup.sh 
  
  Now you have to run them through pythia first to get the cross section value for all the events, with such a cfg for example:   Hadronizer_TuneZ2_5TeV_generic_LHE_pythia_cff_py_GEN_SIM.py. If you look at the first few lines of this cfg, then you can see   how to generate it to read lhe files for the cfg you are interested in. 
  like so: 
    Process and cross-section statistics
    ------------------------------------
    Process	events	tried	xsec [pb]		accepted [%]
    10001	189257	189399	2.251e+10 +/- 1.013e+19	99.7
    Total	189257	189399	2.251e+10 +/- 1.013e+19	99.7

  this value of the xsec in pico barns is privided as an input to RIVET during the production: 


RIVET: 
  1) Install Rivet: https://twiki.cern.ch/twiki/bin/viewauth/CMS/Rivet 
  2) Get this repository which contains the necessary files and analyzer to look at the object you are interested in. 
      Also take a look at the https://rivet.hepforge.org/analyses to see if any analysis does exactly what you want to do, in         that case you can download that analysis.  
      I used a modified version of the CMSSW_TEST_ANALYSIS.cc analyzer for my purposes, which was to generate inclusive jet           spectra 
  3) once you create/modify the analyzer, then compile $ scram b -j20
  4) rivet needs an input aida file which will tells your analyzer about the output histogram format. and rivet histograms are        always named so: d01-x01-y01 and d02-x02-y01 etc... and their bin structure must be clearly defined in the aida file            (which must be located in the GeneratorInterface/RivetInterface/data/*.aida) 
  5) Use a cfg file similar to this TuneZ2_MPIoff_powheg_ct10n_5p02TeV.py (available in this repo) where you need to put the          cross section values from the previous pythia generation as an input: 
       process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
       process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_TEST_ANALYSIS')
       process.rivetAnalyzer.CrossSection = cms.double(options.sigma)
       process.rivetAnalyzer.OutputFile = cms.string('CMS_TEST_ANALYSIS_out_ktmin5.aida')
       process.generation_step+=process.rivetAnalyzer
       
  6) rivet automatically normalizes to delta eta and delta pT, if you specify the eta range for each histogram in your analyzer.       so the only normalization you have to worry is about the cross section and the sumOfWeights for all the events.  if you         are generating spectra in absolute rapidity bins, you need to divide by 2. 
  7) Once you are able to run the cfg file and you have created an output aida file, you can convert it to a root file using the       simple command $ aida2root out.aida. this root file will contain the histogram you created in TGraphAsymmErrors format. 
      If you have a .plot file inside GeneratorInterface/RivetInterface/data/ then you can run $ rivet-mkhtml out.aida and that       will create plots for you as well. 
  
  This is all I have at the moment, I will add more comments in the coming days. 
  
