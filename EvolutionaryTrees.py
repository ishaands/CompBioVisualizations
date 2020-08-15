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

#CLUSTALW algos

def sumPairScores(align1, align2, idx1, idx2, match, mismatch, gap):
    alignment1 = ['']*len(align1)
    for i in range(len(align1)):
        alignment1[i] = align1[i][idx1]

    alignment2 = [''] * len(align2)
    for i in range(len(align2)):
        alignment2[i] = align1[i][idx2]

    score = 0.0

    for char in alignment1:
        for char2 in alignment2:
            if char == '-' and char2 == '-':
                continue
            elif char == char2:
                score += match
            elif char != '-' and char2 != '-':
                score -= mismatch
            else:
                score -= gap

    return score

def generateScoreTable(align1, align2, match, mismatch, gap, supergap):
    scoreTable = [[0 for i in range(len(align1[0]) + 1)] for j in range(len(align2[0]) + 1)]

    for i in range(len(scoreTable)):
        scoreTable[i][0] = i * (-supergap)
    for i in range(len(scoreTable[0])):
        scoreTable[0][i] = i * (-supergap)

    for i in range(1, len(align1[0]) + 1):
        for j in range(1, len(align2[0]) + 1):

            up = scoreTable[i-1][j] - supergap
            left = scoreTable[i][j-1] - supergap
            diag = scoreTable[i-1][j-1] + sumPairScores(align1, align2, i-1, j-1, match, mismatch, gap)

            scoreTable[i][j] = max(up, left, diag)

    return scoreTable

def progressiveBacktrack(scoreTable, align1, align2, match, mismatch, gap, supergap):
    numRows = len(align1[0]) + 1
    numCols = len(align2[0]) + 1

    backtrack = [['' for i in range(numRows)] for j in range(numCols)]

    for i in range(1, numCols):
        backtrack[0][i] = "LEFT"
    for i in range(1, numRows):
        backtrack[i][0] = "UP"

    for i in range(1, numRows):
        for j in range(1, numCols):
            if (scoreTable[i][j] == scoreTable[i-1][j] - supergap):
                backtrack[i][j] = "UP"
            elif scoreTable[i][j] == scoreTable[i][j-1] - supergap:
                backtrack[i][j] = "LEFT"
            else:
                backtrack[i][j] = "DIAG"

    return backtrack

def backtracker(string, backtrack, orientation):
    aligned = ""

    row = len(backtrack) - 1
    col = len(backtrack[0]) - 1

    while(row != 0 or col != 0):
        k = len(string)

        if backtrack[row][col] == "UP":
            if (orientation == "top"):
                aligned = "-" + aligned
            elif orientation == "side":
                aligned = str(string[k - 1]) + aligned
                string = string[:k - 1]
            row -= 1
        elif backtrack[row][col] == "LEFT":
            if (orientation == "side"):
                aligned = "-" + aligned
            elif orientation == "top":
                aligned = str(string[k-1]) + aligned
                string = string[:k-1]
            col -= 1
        else:
            aligned = str(string[k-1]) + aligned
            string = string[:k-1]
            row -= 1
            col -= 1

    return aligned

def outputProgressiveAlign(align1, align2, backtrack):
    a = [[""] for i in range(len(align1) + len(align2))]

    for i in range(len(align1)):
        a[i] = backtracker(align1[i], backtrack, "side")
    for j in range(len(align1), len(align2) + len(align1)):
        a[j] = backtracker(align2[j - len(align1)], backtrack, "top")

    return a

def progressiveAlign(align1, align2, match, mismatch, gap, supergap):
    scoreTable = generateScoreTable(align1, align2, match, mismatch, gap, supergap)
    backtrack = progressiveBacktrack(scoreTable, align1, align2, match, mismatch, gap, supergap)
    opt = outputProgressiveAlign(align1, align2, backtrack)

    return opt

def clustalw(guideTree, dnaStrings, match, mismatch, gap, supergap):

    for i in range(len(dnaStrings)):
        guideTree[i].alignment = [dnaStrings[i]]

    for j in range(len(dnaStrings), len(guideTree)):
        child1 = guideTree[j].child1
        child2 = guideTree[j].child2

        guideTree[j].alignment = progressiveAlign(child1.alignment, child2.alignment, match, mismatch, gap, supergap)

    return guideTree[len(guideTree) - 1].alignment

#main
if __name__ == "__main__":
    print("UPGMA Test")
    mtx = [[0, 3, 4, 3], [3, 0, 4, 5], [4, 4, 0, 2], [3, 5, 2, 0]]
    labels = ["H", "C", "W", "S"]
    tree = upgma(mtx, labels)

    print("CLUSTALW Test")

    match = 1.0
    mismatch = 1.0
    gap = 6.0
    supergap = 10.0

    dnaStrings = ["ATGCATGC", "ATCCATGC", "TACGATGC", "TAAGATGC"]
    alignment = clustalw(tree, dnaStrings, match, mismatch, gap, supergap)
    print(alignment)