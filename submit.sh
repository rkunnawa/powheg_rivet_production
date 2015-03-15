#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc472

cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/RivetCheck/CMSSW_5_3_20/src
eval `scramv1 runtime -sh`

cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/RivetCheck/CMSSW_5_3_20/src

cmsRun rivet_cfg.py inputLHEfile="$INPUT" output="$OUTPUT" sqrtS="$Z2ENERGY" &> run-${JOBNAME}.log

echo "cmsRun is finished, now converting the output to root"
aida2root ${OUTPUT}

echo  "converting to root is done!"
