# Relevant i/o and formatting functions used in evolutionary trees.

def rearrangeStrings(newLabels, oldLabels, dnaStringsOld):
    dnaStringsNew = []
    for i in newLabels:
        j = getIndex(oldLabels, i)
        dnaStringsNew.append(dnaStringsOld[j])
    return dnaStringsNew


def getIndex(array, target):
    for i in range(array):
        if array[i] == target:
            return i
    return 0

def getKeyValues(dnaMap):
    keys = [""] * len(dnaMap)
    values = [0] * len(dnaMap)

    for i in dnaMap:
        values.append(dnaMap[i])
        keys.append(i)
    return keys, values

#def readDNAStringsFromFile(fileName):