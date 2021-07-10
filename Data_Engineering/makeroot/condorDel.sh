#!/bin/bash

Delphes="/home/dylee/tools/Delphes3.4.2/"

cat << EOF > runCondorDelPy_${1%.*}.sh
#!/bin/bash

filename=\`basename \${1}\`
process=\${filename%.*}

export SCRAM_ARCH=slc6_amd64_gcc530
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
echo "\$VO_CMS_SW_DIR \$SCRAM_ARCH"
source \$VO_CMS_SW_DIR/cmsset_default.sh

cd /home/dylee/tools/CMSSW_9_1_0_pre3
eval \`scramv1 runtime -sh\`
cd -

export PYTHIA8=/cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/pythia8/223-mlhled
export PYTHIA8DATA=\$PYTHIA8/share/Pythia8/xmldoc/
export LD_LIBRARY_PATH=\$PYTHIA8/lib:\$LD_LIBRARY_PATH

cat << EOF > config.cmnd
! 1) Settings used in the main program.

Main:numberOfEvents = 10000            ! number of events to generate
Main:timesAllowErrors = 3          ! how many aborts before run stops

! 2) Settings related to output in init(), next() and stat().

Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 200             ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

! 3) Set the input LHE file

Beams:frameType = 4
Beams:LHEF = \${PWD}/\${filename}
$(echo 'EOF')

if [ ! -d condorDelPyOut ]; then mkdir condorDelPyOut; fi
cp config.cmnd condorDelPyOut/

ls

${Delphes}DelphesPythia8 ${Delphes}cards/CMS_PhaseII/CMS_PhaseII_200PU_v03.tcl config.cmnd DelPy_\${process}.root

mv DelPy_\${process}.root condorDelPyOut/
EOF

chmod +x runCondorDelPy_${1%.*}.sh

cat << EOF > job_${1%.*}.jdl
executable = runCondorDelPy_${1%.*}.sh
universe = vanilla
output   = condorDelPyLog/condorDelPyLog.log
error    = condorDelPyLog/condorDelPyLog.err
log      = /dev/null
should_transfer_files = yes
requirements = (machine == "node01")||(machine == "node02")||(machine == "node03")||(machine == "node04")||(machine=="node05")
transfer_input_files = ${Delphes}cards/CMS_PhaseII/CMS_PhaseII_200PU_v03.tcl, /x4/cms/dylee/MinBias_100k.pileup, \$(DATAFile)
when_to_transfer_output = ON_EXIT
transfer_output_files = condorDelPyOut
arguments = \$(DATAFile) 
queue DATAFile from ${1}
EOF
if [ ! -d condorDelPyLog ]; then mkdir condorDelPyLog; fi

condor_submit job_${1%.*}.jdl

