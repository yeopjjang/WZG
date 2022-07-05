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

output=`echo $gridpack | awk -F '/' '{print $9}' | awk -F '_sl' '{print $1}'`

N_gen=10000
N_queue=9

#gridpackname=`basename $gridpack`

# Make excution file
cat << EOF > runCondor_${output}.sh
#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
tar xvf `basename $gridpack`
./runcmsgrid.sh $N_gen \$RANDOM
if [ ! -d lheOut ]; then mkdir lheOut; fi
mv cmsgrid_final.lhe lheOut/${output}_\$1_\$2.lhe
EOF
chmod   +x runCondor_${output}.sh


# Make description file
cat << EOF > job_${output}.jdl
executable = runCondor_${output}.sh
universe = vanilla
output   = lheLog/${output}_\$(Cluster)_\$(Process).log
error    = lheLog/${output}_\$(Cluster)_\$(Process).log
log      = /dev/null
should_transfer_files = yes
requirements = (machine == "node01")||(machine == "node02")||(machine == "node03")||(machine == "node04")||(machine == "node05")||(machine == "node07")
transfer_input_files = $gridpack
when_to_transfer_output = ON_EXIT
transfer_output_files = lheOut
arguments = \$(Cluster) \$(Process) 
queue $N_queue
EOF
if [ ! -d lheLog ]; then mkdir lheLog; fi

# Submit job
condor_submit job_${output}.jdl

