#!/usr/env/bin
#-*-coding:utf8-*-

import numpy as np
import string
from pca import *

if __name__ == '__main__':

    sourcefile = '../data/microarray.original.txt'
    f = open(sourcefile,'r')
    f.readline()

    print "Now reading data..."

    ######test######

    # num = 0
    # for i in range(0,22283):
    #     line = f.readline()
    #     line = line[:-1].split('\t')
    #     # line = map(string.atof,line[1:])
    #     if string.atof(line[1])>=5:
    #         num+=1
    ######test######

    num = 0
    data = []
    for i in range(0,22283):
        line = f.readline()
        line = line[:-1].split('\t')
        if string.atof(line[1])<10:
            continue
        num+=1
        line = line[1:]
        line = map(string.atof,line)
        data.append(line)

    f.close()
    print "Data has been read successfully."
    print "The dimension is "+str(num)

    data = np.array(data).T
    print "Now reducing dimension..."
    lowDData = pca(data,0.90)
    print "Finished, the new dimension is :"+str(len(lowDData[0]))

    print "Start writing new data..."
    destfile = '../data/data_dimRed.txt'
    f = open(destfile,'wb')
    for i in range(0,len(lowDData)):
        for j in range(0,len(lowDData[i])):
            f.write(str(lowDData[i][j])+'\t')
        f.write('\n')

    print "Finished the whole work."

    # testArray = np.array([[4,3,2],[3,2,1],[2,0,0]])
    # lowd,res = pca(testArray)
    # print res
