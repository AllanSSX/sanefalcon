#!/bin/bash

INDIR=$1
OUTDIR=$2
mkdir $OUTDIR

export SANEFALCON=/home/acormier/working_directory/DPNI/sanefalcon
export RETRO=${SANEFALCON}/retro.py

for SAMPLE in `find $INDIR -name "*.bam"`
do
    SHORT=$(basename $SAMPLE)
    OUTFILE="$OUTDIR/${SHORT}"
    echo "IN:$SAMPLE, OUT:$OUTFILE"
    
    for ARG_TASKID in `seq 1 22` # or "X"
    do
        samtools view $SAMPLE chr$ARG_TASKID -F 20 -q 1 | python $RETRO | awk '{print $4}' > $OUTFILE.$ARG_TASKID.start.fwd &
        samtools view $SAMPLE chr$ARG_TASKID -f 16 -F 4 -q 1 | python $RETRO | awk '{print ($4 + length($10) - 1)}' > $OUTFILE.$ARG_TASKID.start.rev
    done
done