#!/usr/bin/env python
# -*- coding: utf-8 -*-

#________________________________________________________________________________________________________________________________#

from joblib import Parallel, delayed  
import subprocess
import os
import sys

#________________________________________________________________________________________________________________________________#

def getProfiles(sample):
        
        input = sys.argv[1]
        output = sys.argv[2]
        
        nuclTrak = '/home/acormier/working_directory/DPNI/data/roy-nucleosome-track'
        getProfile = '/NGS/Various/DPNI/sanefalcon/getProfile.py'
        
        name, chr, type, strand = sample.split('.')
        
        if strand == 'fwd':
                cmd_0 = "python {getProfile} {nuclTrak}/nucl_exR.{chr} {input}/{name}.{chr}.start.fwd 0 {output}/{name}.{chr}.fwd".format(getProfile=getProfile, nuclTrak=nuclTrak, input=input, chr=chr, sample=sample, name=name, output=output)
                cmd_1 = "python {getProfile} {nuclTrak}/nucl_exR.{chr} {input}/{name}.{chr}.start.fwd 1 {output}/{name}.{chr}.ifwd".format(getProfile=getProfile, nuclTrak=nuclTrak, input=input, chr=chr, sample=sample, name=name, output=output)
                
                process = subprocess.Popen(cmd_0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                
                process = subprocess.Popen(cmd_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.communicate()
                
        elif strand == 'rev':
               cmd_0 = "python {getProfile} {nuclTrak}/nucl_exR.{chr} {input}/{name}.{chr}.start.rev 1 {output}/{name}.{chr}.rev".format(getProfile=getProfile, nuclTrak=nuclTrak, input=input, chr=chr, sample=sample, name=name, output=output)
               cmd_1 = "python {getProfile} {nuclTrak}/nucl_exR.{chr} {input}/{name}.{chr}.start.rev 0 {output}/{name}.{chr}.irev".format(getProfile=getProfile, nuclTrak=nuclTrak, input=input, chr=chr, sample=sample, name=name, output=output)
               
               process = subprocess.Popen(cmd_0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               process.communicate()
               
               process = subprocess.Popen(cmd_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               process.communicate()

def main():
        
        num_cores=30
        
        input = sys.argv[1]
        output = sys.argv[2]
        
        samples = os.listdir(input)
                
        Parallel(n_jobs=num_cores)(delayed(getProfiles)(sample) for sample in samples)  

if __name__ == '__main__':
        main()
