#!/usr/bin/python3
import math
import random
import matplotlib.pyplot as plt
import argparse

def calcRMSD(G):
    ''' calculate RMSD of list G with respect to (0,0,0,...0)'''
    sumG2 = sum(map(lambda x: x * x, G))
    return math.sqrt(sumG2 / len(G))

def readFrame(input):
    ''' read a frame,
        return RMSD(G) '''

    G = []
    while True:
        line = input.readline().strip().split()
        if line == []:
            break
        if line[0].startswith('#'):
            continue

        G.append(float(line[1]))

    if G != []:
        return calcRMSD(G)
    else:
        return False

def parseHistFile(input):
    ''' read a hist.czar.pmf file
        return a list about RMSD of each frame '''
    rmsd = []
    with open(input, 'r') as ifile:
        while True:
            rmsdPerFrame = readFrame(ifile)
            if rmsdPerFrame is False:
                break
            rmsd.append(rmsdPerFrame)
    return rmsd

def convergence(input):
    ''' plot the time evolution of PMF rmsd '''
    rmsdList = parseHistFile(input)
    plt.plot(range(1, len(rmsdList) + 1), rmsdList)
    plt.xlabel('Frame')
    plt.ylabel('RMSD (Colvars Unit)')
    plt.show()

def plotMultipleLines(x, y):
    ''' plot multiple lines '''
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(x)):
        for j in range(len(y)):
            plt.plot(x[i], y[i], random.choice(color))
    plt.show()

def plotMergedWindows(args, pmf = False):
    ''' plot pmf, count or grad from a series of files '''
    x = []
    y = []

    ylast = 0
    yfirst = 0
    for inputFile in args:
        with open(inputFile, 'r') as ifile:
            xi = []
            yi = []

            if pmf == False:
                # skip the head of grad or count file
                line = ifile.readline().strip().split()
                line = ifile.readline().strip().split()
                line = ifile.readline().strip().split()

            while True:
                line = ifile.readline().strip().split()
                if line == []:
                    ylast = yi[-1]
                    break
                if line[0].startswith('#'):
                    continue
                if yi == [] and pmf == True:
                    yfirst = float(line[1])
                
                xi.append(float(line[0]))
                if pmf == True:
                    yi.append(float(line[1]) + ylast - yfirst)
                else:
                    yi.append(float(line[1]))
                
            x.append(xi)
            y.append(yi)

    plotMultipleLines(x, y)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-hist', nargs = 1)
    parser.add_argument('-pmf', nargs = '+')
    parser.add_argument('-count', nargs = '+')
    parser.add_argument('-grad', nargs = '+')
    args = parser.parse_args()
    if args.hist:
        convergence(args.hist[0])
    if args.pmf:
        plotMergedWindows(args.pmf, pmf = True)
    if args.count:
        plotMergedWindows(args.count)
    if args.grad:
        plotMergedWindows(args.grad)
