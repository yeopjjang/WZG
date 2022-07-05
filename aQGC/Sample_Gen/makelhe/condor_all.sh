#!bin/bash

for dir in $(ls -ld /x6/spool/dylee/workspace/aQGC/gridpack/FM0/ | grep "^d" | awk '{print $9}') ;do

	for tar in $dir*; do
		source run_condor.sh $tar
        
done
done

