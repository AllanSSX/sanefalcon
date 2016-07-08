#!/usr/bin/env python
# -*- coding: utf-8 -*-

#================================================================#

import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#================================================================#

def getArgs():
    parser = argparse.ArgumentParser(description="",version="1.0.0")
    parser.add_argument('-u',dest="up",type=argparse.FileType('r'),required=True,help='upstream csv file')
    parser.add_argument('-d',dest="down",type=argparse.FileType('r'),required=True,help='downstream csv file')
    
    args = parser.parse_args()

    return args

def splitcsv(csv):
    csvdict = {}
    
    for line in csv:
        elem = line.split(',')
        id = elem[0]
        pos = map(float, elem[1:-1])
        csvdict[id] = pos
    
    return csvdict

def main(args):
    up = splitcsv(args.up)
    down = splitcsv(args.down)
    
    plt.figure(figsize=(16, 4))
    for sample in sorted(up.keys()):
        
        upPos = up[sample]
        upPos.reverse()
        downPos = down[sample]
        
        # 1 / 
        profiles = [sample] + upPos[:-1] + downPos
        print ','.join(map(str, profiles))
        
        # 2 / 
        profiles = upPos[:-1] + downPos
        sumReads = sum(profiles)
        tmplst = []
        for reads in (profiles):
            tmplst.append(reads/sumReads)
        plt.plot(tmplst)
    
    plt.xlim([0,292])
    center = 147-1
    plt.xticks([0,center-93, center-73,center, center+73,center+93,len(tmplst)-1],['\nUpstream','93','73\nStart','0\nCenter','73\nEnd','93','\nDownstream'])
    plt.axvline(x=center-93, linewidth=1, ls='--', color = 'k')
    plt.axvline(x=center-73, linewidth=1, ls='--', color = 'k')
    plt.axvline(x=center, linewidth=1, ls='--', color = 'k')
    plt.axvline(x=center+73, linewidth=1, ls='--', color = 'k')
    plt.axvline(x=center+93, linewidth=1, ls='--', color = 'k')
    
    plt.title("Nucleosome Profile")
    plt.xlabel("Nucleosome BP Position")
    plt.ylabel("Ratio")  
    plt.savefig("nuclProfiles.pdf", dpi=400)
  
if __name__ == '__main__':
    args = getArgs()
    main(args)