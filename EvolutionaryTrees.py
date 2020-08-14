# Evolutionary Trees contains algorithms and methods used in determining phylogenetic inheritance of various species.
# Main algos UPGMA and CLUSTALW
from dataclasses import dataclass

@dataclass
class Node:
    age: int
    num: int
    label: str
    alignment: []
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
    clusters = [0]*int(numLeaves)

    for i in range(int(numLeaves)):
        clusters[i] = t[i]

    return clusters

def initializeTree(speciesNames):
    numLeaves = len(speciesNames)

    t = [Node]*(2*numLeaves - 1)

    for i in range(len(t)):
        vx = Node()

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
    del clusters[col]
    del clusters[row]
    return clusters

def findMinElement(mtx):
    minRow = 0
    minCol = 1
    minElement = mtx[0][1]
    for row in range(0, len(mtx)):
        for col in range(row+1, len(mtx)):
            if mtx[row][col] < minElement:
                minRow = row
                minCol = col
                minElement = mtx[row][col]

    return minRow, minCol, minElement

def delRowCol(mtx, row, col):
    del mtx[col]
    del mtx[row]

    for i in range(len(mtx)):
        del mtx[i][col]
        del mtx[i][row]

    return mtx

def addRowCol(mtx, clusters, row, col):
    newRow = [0]*(len(mtx) + 1)

    for i in range(len(newRow) - 1):
        if i != row and i != col:
            size1 = countLeaves(clusters[row])
            size2 = countLeaves(clusters[col])
            avg = (size1*mtx[row][i] + size2*mtx[i][col]) / (size1 + size2)
            newRow[i] = avg

    mtx.append(newRow)

    for i in range(len(newRow) - 1):
        mtx[i].append(newRow[i])

    return mtx

def upgma(mtx, speciesNames):
    tree = initializeTree(speciesNames)
    clusters = initializeClusters(tree)
    numLeaves = len(mtx)

    for i in range(numLeaves, 2*numLeaves - 1):
        minElements = findMinElement(mtx)
        row = minElements[0]
        col = minElements[1]
        min = minElements[2]

        tree[i].age = min/2
        tree[i].child1 = clusters[row]
        tree[i].child2 = clusters[col]

        mtx = addRowCol(mtx, clusters, row, col)
        clusters.append(tree[i])
        mtx = delRowCol(mtx, row, col)

        clusters = delClusters(clusters, row, col)

    return tree

if __name__ == "__main__":
    print("UPGMA Test")
    mtx = [[0, 3, 4, 3], [3, 0, 4, 5], [4, 4, 0, 2], [3, 5, 2, 0]]
    labels = ["H", "C", "W", "S"]
    tree = upgma(mtx, labels)

#CLUSTALW algos