# Evolutionary Trees contains algorithms and methods used in determining phylogenetic inheritance of various species.
# Main algos UPGMA and CLUSTALW
from dataclasses import dataclass

@dataclass
class Node:
    num: int
    age: float
    label: str
    alignment: list
    def __init__(self, child1=None, child2=None):
        self.child1 = child1
        self.child2 = child2


#UPGMA algos

def initializeMatrix(m, n):
    mtx = [[0 for x in range(n)] for y in range(m)]
    return mtx

def initializeClusters(t):
    numNodes = len(t)
    numLeaves = (numNodes + 1) / 2
    clusters = [numLeaves]

    for i in range(int(numLeaves)):
        clusters[int(numLeaves)] = t[i]

    return clusters

def initializeTree(speciesNames):
    numLeaves = len(speciesNames)

    t = [2*numLeaves - 1]

    for i in range(len(t)):
        vx: Node
        if i < numLeaves:
            vx.label = speciesNames[i]
        else:
            vx.label = "Ancestor species" + str(i)
        vx.num = i
        t[i] = vx

    return t

def countLeaves(v: Node):
    if v.child1 is None or v.child2 is None:
        return 1

    return countLeaves(v.child1) + countLeaves(v.child2)

def delClusters(clusters, row, col):
    clusters = clusters[:col].extend(clusters[col+1:])
    clusters = clusters[:row].extend(clusters[row+1:])
    return clusters


#CLUSTALW algos