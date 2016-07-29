#!/bin/bash

LOCREADS="/home/acormier/working_directory/DPNI/data/readStarts"

while IFS=, read -r -a input
do
   echo ${input[1]}
   cd ${input[1]}/readStarts/
   echo ${input[0]}
   tar xzf ${LOCREADS}/${input[0]}.tar.gz
   mv */* .
   cd ../..
done < $1
