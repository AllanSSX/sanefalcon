#!/bin/bash

export SANEFALCON=/NGS/Various/DPNI/sanefalcon
export PROFIL=${SANEFALCON}/getProfile.py

#getProfile
SUBTRAINDIR=$1
SOURCE=$2
READSTARTSDIR="readStarts"
SAMPLEOUT="nucProfile"

for SAMPLE in `find $SUBTRAINDIR -name "*.bam"`
do
    SHORT=$(basename $SAMPLE)
    SHORT="${SHORT%.*}"
    for CHROM in `seq 1 22` # or "X"
        do
            echo "  Working on chrom $CHROM"
            python $PROFIL $SUBTRAINDIR/nucl_ex${SOURCE}.$CHROM $SUBTRAINDIR/$READSTARTSDIR/$SHORT.$CHROM.start.fwd 0 $SUBTRAINDIR/$SAMPLEOUT/$SHORT.$CHROM.fwd
            python $PROFIL $SUBTRAINDIR/nucl_ex${SOURCE}.$CHROM $SUBTRAINDIR/$READSTARTSDIR/$SHORT.$CHROM.start.fwd 1 $SUBTRAINDIR/$SAMPLEOUT/$SHORT.$CHROM.ifwd
            python $PROFIL $SUBTRAINDIR/nucl_ex${SOURCE}.$CHROM $SUBTRAINDIR/$READSTARTSDIR/$SHORT.$CHROM.start.rev 1 $SUBTRAINDIR/$SAMPLEOUT/$SHORT.$CHROM.rev
            python $PROFIL $SUBTRAINDIR/nucl_ex${SOURCE}.$CHROM $SUBTRAINDIR/$READSTARTSDIR/$SHORT.$CHROM.start.rev 0 $SUBTRAINDIR/$SAMPLEOUT/$SHORT.$CHROM.irev
        done
done

