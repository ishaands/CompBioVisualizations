# Richness takes a frequency map(dict). It returns the richness of the frequency map(dict)
# (i.e., the number of keys in the map(dict) corresponding to nonzero values.)
def richness(sample):
    count = 0

    for freq in sample.values():
        if freq > 0:
            count += 1

    return count


# Multiple Richness
def richnessMatrix(allMaps):
    arr = []

    for freqMap in allMaps:
        arr.append(richness(freqMap))

    return arr


# Evenness
def simpsonsIndex(sample):
    total = 0

    for freq in sample.values():
        total += freq

    sIndex = 0.0

    for freq in sample.values():
        sIndex += pow(float(freq) / float(total), 2.0)

    return sIndex


# Multiple Evenness
def simsonsMatrix(allMaps):
    arr = []

    for freqMap in allMaps:
        arr.append(simpsonsIndex(freqMap))

    return arr


def frequencyMap(arr):
    freqMap = {}

    for val in arr:
        if val in freqMap.keys():
            freqMap[val] += 1
        else:
            freqMap[val] = 1

    return freqMap


def jaccardDistance(sample1, sample2):
    sumOfMins = 0
    sumOfMaxs = 0

    for key, val1 in sample1:
        if key in sample2.keys():
            val2 = sample2[key]
            sumOfMins += MinTwo(val1, val2)
            sumOfMaxs += MaxTwo(val1, val2)
        else:
            sumOfMaxs += val1

    for key, val2 in sample2:
        if key in sample1.keys():
            sumOfMaxs += val2

    return 1 - float(sumOfMins) / float(sumOfMaxs)


def MinTwo(a, b):
    if a < b:
        return a
    return b


def MaxTwo(a, b):
    if a > b:
        return a
    return b


def brayCurtisDistance(sample1, sample2):
    sumOfMins = 0
    total = 0

    for key, val1 in sample1:
        if key in sample2.keys():
            val2 = sample2[key]
            sumOfMins += MinTwo(val1, val2)
            total += val1 + val2
        else:
            total += val1

    for key, val2 in sample2:
        if key in sample1.keys():
            total += val2

    avg = float(total) / 2.0
    return 1 - float(sumOfMins) / avg