# Relevant i/o and formatting functions used in evolutionary trees.

def rearrangeStrings(newLabels, oldLabels, dnaStringsOld):
    dnaStringsNew = []
    for i in newLabels:
        j = getIndex(oldLabels, i)
        dnaStringsNew.append(dnaStringsOld[j])
    return dnaStringsNew


def getIndex(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return 0

def getKeyValues(dnaMap):
    keys = []
    values = []

    for i in dnaMap:
        values.append(dnaMap[i])
        keys.append(i)
    return keys, values

def readDNAStringsFromFile(fileName):
    file = open(fileName, 'r')

    lines = file.readlines()
    file.close()

    dnaMap = {}
    curLabel = ""

    for i in range(len(lines)):
        if i % 2 == 0:
            curLabel = lines[i]
        else:
            dnaMap[curLabel] = lines[i]
    return dnaMap

def readMatrixFromFile(filename):
    lines = []
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
    except Exception as e:
        print(e)

    mtx = []
    speciesNames = []

    for i in range(len(lines)):
        if i >= 1:
            row = []
            nums = str.split(lines[i], "\t")
            for i in range(len(nums)):
                if i == 0:
                    speciesNames.append(nums[i])
                else:
                    n = float(nums[i])
                    row.append(n)
            mtx.append(row)

    return mtx, speciesNames

def writeAlignmentToFile(align, labels, fileLocation, fileName):
    accum = ""
    for i in range(len(align)):
        accum += ">" + labels[i] + "\n"
        accum += align[i] + "\n"
    file = open(fileLocation + "/" + fileName, 'w')
    try:
        file.write(accum)
        file.close()
        print("success")
    except Exception as e:
        print(e)

