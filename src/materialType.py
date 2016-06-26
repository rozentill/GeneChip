#!/usr/env/bin
#-*-coding:utf8-*-

import numpy as np
import string
import net

if __name__ == '__main__':

    numTrain = 5896
    numTest = 5896
    iteration = 40
    rate = 0.05
    errorTrain = 0
    errorTest = 0

    # data_x = []
    # data_y = []

    NN = net.BPANN(112,3,1,1,rate,1,1)
    NN.numTrain = numTrain
    NN.numTest = numTest

    #train
    for k in range(0,iteration):

        fy = open('../data/E-TABM-185.sdrf.txt','r')
        fx = open('../data/data_dimRed.txt','r')
        fy.readline()
        errorTrain = 0
        for i in range(0,5896):
            line_x = fx.readline().split('\t')[:-1]
            line_x = map(string.atof,line_x)
            line_y = fy.readline().split('\t')[1:2][0]

            if line_y == 'organism_part':
                line_y = [1]
            else :
                line_y = [-1]
            # print "this train sample is :" + str(line_y[0])

            NN.train(line_x,line_y)

            errorTrain += NN.train_error**2

        print "the train error is :"+str(errorTrain/(2*numTrain))
        fx.close()
        fy.close()

    fy = open('../data/E-TABM-185.sdrf.txt','r')
    fx = open('../data/data_dimRed.txt','r')
    fy.readline()
    #test
    hit = 0
    for j in range(0,5896):
        line_x = fx.readline().split('\t')[:-1]
        line_x = map(string.atof,line_x)
        line_y = fy.readline().split('\t')[1:2][0]

        if line_y == 'organism_part':
            line_y = [1]
        else :
            line_y = [-1]

        dataOutput = NN.test(line_x)
        if (dataOutput[0]>=0 and line_y[0]==1)or(dataOutput[0]<0 and line_y[0]==-1):
            hit += 1
        NN.test_error = line_y[0]-dataOutput[0]
        errorTest += NN.test_error**2

    print "the test error is :"+str(errorTest/(2*numTest))
    print "the hit rate is :"+str(hit/float(numTest))

    fx.close()
    fy.close()
