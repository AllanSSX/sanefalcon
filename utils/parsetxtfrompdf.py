#!/usr/bin/python
# -*- coding: utf-8 -*-

#================================================================#

import argparse

#================================================================#

def getArgs():
    parser = argparse.ArgumentParser(description="",version="1.0.0")
    parser.add_argument('-i',dest="txt",type=argparse.FileType('r'),required=True,help='')
    arg = parser.parse_args()

    return arg

def main(args):
    
    i=1
    tmp = []
    for line in args.txt:
        info = line.split()
        if i == 1:
            tmp.append(info[3])
        elif i == 60 and info[0] in ['Yes', 'No','Undetermined']:
            tmp.append(info[0])
        elif i == 61 and info[0]:# in ['Yes', 'No','Undetermined']:
            tmp.append(info[0])
        elif i == 62 and line[:-1] != '':
            tmp.append(info[0])
        
        i += 1
    
    print '\t'.join(tmp)
 

if __name__ == '__main__':
    args = getArgs()
    main(args)