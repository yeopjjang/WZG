#!/bin/bash

for ((first=-6; first<-1; first+=1)); do
for ((second=9; second<10; second+=1)); do

echo "FM0_${first}_${second}"
cd ../FM0
mkdir "FM0_${first}_${second}"
cd ../makeFM0
python make_param_card.py ${first} ${second}
python make_proc_card.py ${first} ${second}
python make_run_card.py ${first} ${second}
cd ..
./gridpack_generation.sh "FM0_${first}_${second}" FM0/"FM0_${first}_${second}"
cd /x6/spool/dylee/genproductions/bin/MadGraph5_aMCatNLO/makeFM0
done
done
