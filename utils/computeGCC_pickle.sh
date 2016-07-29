#!/bin/bash

bam=$1
wisecondor="/home/acormier/working_directory/ionplugins/ion-wisecondor/wisecondor"
gccount="/home/acormier/working_directory/ionplugins/ion-wisecondor/data/hg19.gccount"
name=`basename $bam`
name=${name%.*}

samtools view ${bam} -q 1 | python ${wisecondor}/consam.py -outfile ${name}.pickle
python ${wisecondor}/gcc.py  ${name}.pickle ${gccount} ${name}.gcc

