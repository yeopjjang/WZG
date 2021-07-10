#!bin/bash

for dir in $(ls -ld /x4/cms/dylee/Delphes/data/condor/condorplace/signal/lhe/* | grep "^d" | awk '{print $9}') ;do
	echo $dir
		ls -d $dir/events*.lhe > `basename $dir`.list
		source condorDel.sh `basename $dir`.list
		echo "MUYAHO!"
done
