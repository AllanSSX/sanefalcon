#!/bin/bash

bam=$1
name=`basename $bam`
name=${name%.*}

export SANEFALCON=/home/acormier/working_directory/DPNI/sanefalcon
export RETRO=${SANEFALCON}/retro.py

for ARG_TASKID in `seq 1 22` # or "X"
    do
        samtools view $bam chr$ARG_TASKID -F 20 -q 1 | \
        python $RETRO | \
        awk '{print $4}' > $name.$ARG_TASKID.start.fwd &

        samtools view $bam chr$ARG_TASKID -f 16 -F 4 -q 1 | \
        python $RETRO | \
        awk '{print ($4 + length($10) - 1)}' > $name.$ARG_TASKID.start.rev
    done
