#!/bin/bash
#$1 number of jobs
pwd=`pwd`

cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/CMSSW_5_3_20/src/
eval `scramv1 runtime -sh`

source setup.sh

#source /afs/cern.ch/sw/lcg/external/MCGenerators/powheg-box/r2092/x86_64-slc6-gcc46-opt/bin/setup.sh

#cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/CMSSW_5_3_20/src/Appeltel/GenJetCrossCheckAnalyzer/test/POWHEG_BOX/POWHEG-BOX/Dijet/testrun-lhc/test/manyjobs/

cd $pwd

njobs=$1
#dir="Out_"`date +"%F_%T"`
#mkdir $dir
for i in `seq 50 $njobs`; do
jobname=powheg_Job_${i}
seed=1010${i}
export LS_JOBNAME=${jobname}
export LS_SEED=${seed}
echo $LS_SEED
# bsub -q 1nd -o /dev/null -J powheg < powheg.sub
bsub -q 1nd -J powheg_${i} < powheg.sub
done 
