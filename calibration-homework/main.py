'''
Created on 10 janv. 2014

@author: julestestard
'''

import sys
import os

def hasTriangleList(adjlist):
    for u, edgeList in adjlist.iteritems():
        for v in edgeList:
            for w in adjlist[v]:
                if u in adjlist[w]:
                    return True    
    return False

def printMatrix(adjMatrix):
    string = "Matrix : \n"
    for row in adjMatrix:
        for cell in row:
            string += str(cell) + " "
        string+="\n"
    print string

def hasTriangleMatrix(adjMatrix,size):
    for u in xrange(0,size):
        for v in xrange(0,size):
            if adjMatrix[u][v]==1:
                #edge u,v exisits.
                for w in xrange(0,size):
                    if adjMatrix[v][w]==1:
                        #edge v,w
                        for k in xrange(0,size):
                            if adjMatrix[w][k]==1 and k==u:
                                #edge w,u exists
                                return "has a triangle."
    return "does not have a triangle"

if __name__ == '__main__':
    currentdir = os.path.dirname(os.path.realpath(__file__))
    filename = currentdir+"/"+sys.argv[1]
    with open(filename) as f:
        nodeSize, edgeSize = map(lambda x: int(x),f.readline().split(" ")) #Handle first line
        adjMatrix = []
        for i in xrange(0,nodeSize):
            adjMatrix.append([0]*nodeSize) #empty adj matrix with all 0's
        for line in f:
            i , j , dontcare = map(lambda x: int(x)-1,line.split(" "))
            adjMatrix[i][j]=1
        printMatrix(adjMatrix)
        print "Graph for file : {} {}".format(filename,hasTriangleMatrix(adjMatrix,nodeSize))