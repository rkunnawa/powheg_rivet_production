# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/MinBias_TuneZ2_7TeV_pythia6_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 1000 --python_filename=TuneZ2_7TeV_cfg.py --customise=Configuration/GenProduction/rivet_customize_Z2_7TeV.py
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

import os
import random
import time

process = cms.Process('GEN')
options = VarParsing.VarParsing ('standard')

options.output = 'Powheg_5TeV_Pythia_TuneZ2_GEN_LHE_bornkTsupp250_ktmin100.root'
options.maxEvents = 5000

options.register('processType',
                 "NSD",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Pythia process type with pT_hat range")

options.register('sqrtS',
                 5020.0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Center-of-mass energy")

options.register('sigma',
                 2662.9437,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Cross section value from powheg in Nano Barns")

options.register('ptHatLow',
                 1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Minimum pt-hat")

options.register('ptHatHigh',
                 1000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum pt-hat")

options.register('lhefile',
                 "file:pwgevents.lhe",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "pthat in the lhe file")

options.parseArguments()


process.source = cms.Source("LHESource",
                            fileNames = cms.untracked.vstring(options.lhefile)
)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#process.RandomNumberGeneratorService.generator.initialSeed = int(os.getenv('SEED'))

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('PYTHIA6-MinBias TuneZ2 at 7TeV'),
    name = cms.untracked.string('$Source:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/CMSSW_5_3_8_HI_patch2/src/Appeltel/GenJetCrossCheckAnalyzer/test/Powheg_test/TuneZ2_MPIoff_powheg_ct10n_5p02TeV.py $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string(options.output),
                                        dataset = cms.untracked.PSet(
                                                filterName = cms.untracked.string(''),
                                                dataTier = cms.untracked.string('GEN-SIM-RAW')
                                        ),
                                        SelectEvents = cms.untracked.PSet(
                                                SelectEvents = cms.vstring('generation_step')
                                        )
                                )

# Additional output definition

# Other statements

process.GlobalTag.globaltag = 'STARTHI53_V27::All'
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.generator = cms.EDFilter("Pythia6HadronizerFilter",
                                 pythiaPylistVerbosity = cms.untracked.int32(1),
                                 filterEfficiency = cms.untracked.double(1.0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 comEnergy = cms.double(options.sqrtS),
                                 #crossSection = cms.untracked.double(2980000000.0),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 PythiaParameters = cms.PSet(
                                         pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
                                                                        'MSTJ(22)=2     ! Decay those unstable particles', 
                                                                        'PARJ(71)=10 .  ! for which ctau  10 mm', 
                                                                        'MSTP(33)=0     ! no K factors in hard cross sections', 
                                                                        'MSTP(2)=1      ! which order running alphaS', 
                                                                        'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
                                                                        'MSTP(52)=2     ! work with LHAPDF', 
                                                                        'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
                                                                        'PARP(89)=1800. ! sqrts for which PARP82 is set', 
                                                                        'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
                                                                        'MSTP(95)=6     ! CR (color reconnection parameters)', 
                                                                        'PARP(77)=1.016 ! CR', 
                                                                        'PARP(78)=0.538 ! CR', 
                                                                        'PARP(80)=0.1   ! Prob. colored parton from BBR', 
                                                                        'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
                                                                        'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
                                                                        'PARP(62)=1.025 ! ISR cutoff', 
                                                                        'MSTP(91)=1     ! Gaussian primordial kT', 
                                                                        'PARP(93)=10.0  ! primordial kT-max', 
                                                                        'MSTP(81)=20    ! multiple parton interactions 1 is Pythia default', 
                                                                        'MSTP(82)=4     ! Defines the multi-parton model',
                                                                        'MSTP(86)=1'	 	
                                                                ), #to set the mpi cut smaller than the pt of the hardest jet!
                                         processParameters = cms.vstring('MSEL=0   ! user defined process',),
                                         parameterSets = cms.vstring('pythiaUESettings', 
                                                                     'processParameters')
                                 )
                         )
process.ProductionFilterSequence = cms.Sequence(process.generator)
# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GenProduction.rivet_customize_Z2_7TeV
#from Configuration.GenProduction.rivet_customize_Z2_7TeV import customise 

def customise(process):
        process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_pp_5p02TeV') 	
	process.rivetAnalyzer.CrossSection = cms.double(options.sigma)		
	process.rivetAnalyzer.OutputFile = cms.string('CMS_pp_5p02TeV_out.aida')
        process.generation_step+=process.rivetAnalyzer
        process.schedule.remove(process.RAWSIMoutput_step)
        return(process)

#call to customisation function customise imported from Configuration.GenProduction.rivet_customize_Z2_7TeV
process = customise(process)

# End of customisation functions
