#!/usr/bin/python
# -*- coding: utf-8 -*-

#================================================================#

import os
import re
import json
import subprocess

#================================================================#

def main():
    
    path_run = '/results/analysis/output/Home'
    
    dpniDict = {}
    missingRuns = []
    
    for folder in os.listdir(path_run):
        if os.path.isdir(os.path.join(path_run, folder)):
            if not re.search(r"tn", folder) and (re.search(r"DPNI", folder) or re.search(r"DANNI", folder)) :
                folder_path = os.path.join(path_run, folder)
                if checkRUNfiles(folder_path) == 0:
                    
                    json_file = '%s/ion_params_00.json' % folder_path
                    json_load = json.load(open(json_file))
                    runname = json_load['exp_json']['log']['runname'].split('-201')[0]
                    
                    dpniDict[runname] = []
                    for sample, barcode in json_load['experimentAnalysisSettings']['barcodedSamples'].items():
                        
                        sample_name = sample.replace(' ', '_')
                        barcode_name = barcode['barcodeSampleInfo'].keys()[0]
                        
                        dpniDict[runname].append([path_run, folder, barcode_name, sample])
                        
                else:
                    missingRuns.append(folder)
                    
    for folder in missingRuns:
        print folder 
    
    #for run, design in dpniDict.items():
    #    for sample in design:
    #        bam = sample[0] + '/' + sample[1] + '/' + sample[2] +'_rawlib.bam'
    #        name = run + "_" + sample[3]
    #        
    #        sanefalcon_cmd = "/home/ionadmin/acormier/sanefalcon/prepSamples_ac.sh %s %s" % (bam, name)
    #        print run, name
    #        process = subprocess.Popen(sanefalcon_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #        out, err = process.communicate()
    
    
    

def checkRUNfiles(source):
    for file in os.listdir(source):
        if file.endswith('.bam'):
            return 0
            break     

if __name__ == '__main__':
    main()