#!bin/bash

for dir in $(ls -ld /x6/spool/dylee/workspace/aQGC/condor/condorplace/scan/FM0/additional | grep "^d" | awk '{print $9}') ;do

	ls -d $dir/lheOut/*.lhe > `basename $dir`.list
	source run_condorDel.sh `basename $dir`.list

done
