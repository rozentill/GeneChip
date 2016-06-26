#!/usr/env/bin
#-*-coding:utf8-*-

import numpy as np
import string
from pca import *

if __name__ == '__main__':
    filename = '../data/microarray.original.txt'
    f = open(filename,'r')
    f.readline()

    data = []
    for i in range(0,22283):
        line = f.readline()
        line = line[:-1].split('\t')
        line = line[1:]
        line = map(string.atof,line)
        data.append(line)

    data = np.array(data).T
    lowDData, reconData = pca(data)

    # testArray = np.array([[4,3,2],[3,2,1],[2,0,0]])
    # lowd,res = pca(testArray)
    # print res
