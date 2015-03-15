#!/bin/bash
#$1 number of jobs
cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/RivetCheck/CMSSW_5_3_20/src
eval `scramv1 runtime -sh`

cd /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/RivetCheck/CMSSW_5_3_20/src

export Z2ENERGY=5020.
i=0
while read line; do
    
    export INPUT="$line\n"
    export OUTPUT="TuneZ2_POWHEG_CT10NLO_5p02TeV_supfactor250_ktmin5_file${i}.aida"
    export JOBNAME=RIVET_Job_${i}
    echo "input = ${INPUT} with file ${i}"
    bsub -R "pool>5000" -M 3000000 -q 1nd -J rivet_job_${i} < /afs/cern.ch/work/r/rkunnawa/WORK/RAA/pp_genjets_pythia_NPC/RivetCheck/CMSSW_5_3_20/src/submit.sh
    let "i++"
done < 5p02TeV_bornsupp250_powheg.dat

echo "submit all the RIVET analysis for LHE files !"
