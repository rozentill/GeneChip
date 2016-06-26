#!/usr/env/bin
#-*-coding:utf8-*-

import numpy as np
import string

if __name__ == '__main__':
    fy = open('../data/E-TABM-185.sdrf.txt','r')
    fy.readline()
    CellType = []
    TotalClass = []
    for i in range(0,5896):
        label = fy.readline().split('\t')[1:2][0]
        if label not in CellType:
            CellType.append(label)
            TotalClass.append([])

        idx = CellType.index(label)
        TotalClass[idx].append(i)

    for label in CellType:
        print label+":"+str(len(TotalClass[CellType.index(label)]))

    print CellType
