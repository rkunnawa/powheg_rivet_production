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

options.output = 'Powheg_5TeV_Pythia_TuneZ2_GEN_LHE_bornkTsupp250_ktmin5.root'
options.maxEvents = 500000

options.register('sqrtS',
                 5020.0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Center-of-mass energy")

options.register('sigma',
                 22950000000,
                 #2662.9437,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Cross section value from powheg in pico Barns")

options.parseArguments()

# Input source
process.source = cms.Source("LHESource",
                            fileNames = cms.untracked.vstring(
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_1.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_2.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_3.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_4.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_5.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_6.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_7.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_8.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_9.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_10.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_11.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_12.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_13.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_14.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_15.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_16.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_17.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_18.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_19.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_20.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_21.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_22.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_23.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_24.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_25.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_26.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_27.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_28.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_29.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_30.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_31.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_32.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_33.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_34.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_35.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_36.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_37.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_38.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_39.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_40.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_41.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_42.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_43.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_44.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_45.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_46.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_47.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_48.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_49.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_50.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_51.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_52.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_53.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_54.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_55.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_56.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_57.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_58.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_59.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_60.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_61.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_62.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_63.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_64.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_65.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_66.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_67.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_68.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_69.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_70.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_71.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_72.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_73.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_74.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_75.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_76.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_77.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_78.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_79.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_80.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_81.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_82.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_83.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_84.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_85.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_86.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_87.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_88.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_89.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_90.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_91.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_92.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_93.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_94.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_95.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_96.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_97.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_98.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_99.lhe',
                                    'file:/afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/Powheg_cross_check/POWHEG_JOBS/powheg_Job_100.lhe'          
                            )
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
process.MessageLogger.cerr.FwkReport.reportEvery = 50000

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
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_TEST_ANALYSIS') 	
	process.rivetAnalyzer.CrossSection = cms.double(options.sigma)		
	process.rivetAnalyzer.OutputFile = cms.string('CMS_TEST_ANALYSIS_out_ktmin5.aida')
        process.generation_step+=process.rivetAnalyzer
        process.schedule.remove(process.RAWSIMoutput_step)
        return(process)

#call to customisation function customise imported from Configuration.GenProduction.rivet_customize_Z2_7TeV
process = customise(process)

# End of customisation functions
