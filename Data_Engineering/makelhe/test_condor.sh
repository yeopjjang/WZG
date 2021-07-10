#!/bin/bash


#######################################################
# This code generates more madgraph processes             #
# using gridpack.                                                                         #
# You just edit:                                                                          #
# 1. gridpack name                                                                        #
# 2. Number of generate events of one gen                         #
# 3. Number of queue                                                              #
#                                                                                                         #
# If you choose 2. = 10000 and 3. = 5                             #
# Total # of events = 10000*5 = 50000                             #
#                                                                                                         #
# Usage: ./runCondor.sh PATH_AND_NAME_OF_GRIDPACK         #
#######################################################

if [ ! $1 ]; then echo "usage $0 gridpack"; exit; fi
gridpack=`readlink -e $1`
if [ ! -f $gridpack ] || [ ! $1 ]; then echo "Error NotFound GridPack $1"; exit; fi


N_gen=1
N_queue=1

# Make excution file
cat << EOF > runCondor.sh
#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
tar xvf `basename $gridpack`
./runcmsgrid.sh $N_gen \$RANDOM sex
if [ ! -d condorOut ]; then mkdir condorOut; fi
ls
mv cmsgrid_final.lhe condorOut/events_$3_\${2}.lhe
EOF
chmod   +x runCondor.sh


# Make description file
cat << EOF > job.jdl
executable = runCondor.sh
universe = vanilla
output   = condorLog/condorLog_\$(Cluster)_\$(Process).log
error    = condorLog/condorLog_\$(Cluster)_\$(Process).log
log      = /dev/null
should_transfer_files = yes
transfer_input_files = $gridpack
when_to_transfer_output = ON_EXIT
transfer_output_files = condorOut
arguments = \$(Cluster) \$(Process)
queue $N_queue
EOF
if [ ! -d condorLog ]; then mkdir condorLog; fi

# Submit job
condor_submit job.jdl

