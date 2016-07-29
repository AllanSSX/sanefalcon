#!/bin/bash

for SAMPLE in `find $1 -name "*.1.rev.np"`
do 
    SIMPLE=`echo ${SAMPLE//.1.rev.np/} | rev | cut -d"/" -f1 | rev`
    echo $SIMPLE,`LC_NUMERIC=C awk -F"," '{ for(i=1;i<=NF;i++){ fetal[i]+=$i } } END { for(i=1;i<=NF;i++) {printf "%s,",fetal[i]}; print "";}' \
    ${SAMPLE//.1.rev.np/}.*.rev.np ${SAMPLE//.1.rev.np/}.*.fwd.np`
done