#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import subprocess
import os
import argparse
from shutil import copy2
from shutil import copyfile

SYMBOLS = {
    'customary'     : ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'),
    'customary_ext' : ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa', 'zetta', 'iotta'),
    'iec'           : ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
    'iec_ext'       : ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi', 'zebi', 'yobi'),
}

parser = argparse.ArgumentParser(description='')
parser.add_argument('-1', "--outputfile",     help="The final output file name")
parser.add_argument('-2', "--inputfileone",   help="1st input file")
parser.add_argument('-3', "--inputfiletwo",   help="2nd input file")
parser.add_argument('-a', "--outputfilesize", help="The final output file size")
parser.add_argument('-b', "--inputfileoneloc",   help="1st input file location")
parser.add_argument('-c', "--inputfiletwoloc",   help="2nd input file location")
args = parser.parse_args()


def human2bytes(s):
    init = s
    num = ""
    while s and s[0:1].isdigit() or s[0:1] == '.':
        num += s[0]
        s = s[1:]
    num = float(num)
    letter = s.strip()
    for name, sset in SYMBOLS.items():
        if letter in sset:
            break
    else:
        if letter == 'k':
            sset = SYMBOLS['customary']
            letter = letter.upper()
        else:
            raise ValueError("can't interpret %r" % init)
    prefix = {sset[0]:1}
    for i, s in enumerate(sset[1:]):
        prefix[s] = 1 << (i+1)*10
    return int(num * prefix[letter])



def InsertBin(binFile, targetFile, seekPosition):
    with file(binFile, 'rb') as fh:
        patch1 = fh.read()

    with file(targetFile, 'r+b') as fh:
        # apply patch1
        fh.seek(seekPosition)
        fh.write(patch1)



def CreateTemplate(binFile, size):
    try:
        os.remove(binFile)
    except:
        pass

    open(binFile, 'a').close()

    with open(binFile, 'r+b') as f:
        for x in xrange(size):
            f.write(b'\xFF')


print(args.outputfile)
CreateTemplate(args.outputfile, human2bytes(args.outputfilesize))
InsertBin(args.inputfileone, args.outputfile, human2bytes(args.inputfileoneloc))
InsertBin(args.inputfiletwo, args.outputfile, human2bytes(args.inputfiletwoloc))
sys.exit(0)
