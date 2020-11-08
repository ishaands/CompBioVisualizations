# ~~Alignment algorithms and string comparison variations~~

#Global Alignment
def globalAlignment(str0, str1, match, mismatch, gap):
    backtrack = globalBacktrack(str0, str1, match, mismatch, gap)
    return outputGlobalAlignment(str0, str1, backtrack)

def globalBacktrack(str0, str1, match, mismatch, gap):
    if len(str0) == 0 or len(str1) == 0:
        print("Zero length strings given to globalBacktrack")
        return

    numRows = len(str0) + 1
    numCols = len(str1) + 1
    backtrack = [[0]*numCols for _ in range(numRows)]
    scoringMatrix = globalScoreTable(str0, str1, match, mismatch, gap)

    for i in range(1, numCols):
        backtrack[0][i] = "LEFT"
    for i in range(1, numRows):
        backtrack[i][0] = "UP"
    for i in range(1, numRows):
        for j in range(1, numCols):
            if scoringMatrix[i][j] == scoringMatrix[i-1][j] - gap:
                backtrack[i][j] = "UP"
            elif scoringMatrix[i][j] == scoringMatrix[i][j-1] - gap:
                backtrack[i][j] = "LEFT"
            else:
                backtrack[i][j] = "DIAG"
    print(*backtrack, sep="\n")
    return backtrack

def outputGlobalAlignment(str0, str1, backtrack):
    a0 = ""
    a1 = ""
    while len(str0) > 0 or len(str1) > 0:
        row = len(str0)
        col = len(str1)
        if backtrack[row][col] == "UP":
            a0 = str0[row-1] + a0
            a1 = "-" + a1
            str0 = str0[:len(str0)-1]
        elif backtrack[row][col] == "LEFT":
            a0 = "-" + a0
            a1 = str1[col-1] + a1
            str1 = str1[:len(str1)-1]
        elif backtrack[row][col] == "DIAG":
            a0 = str0[row-1] + a0
            a1 = str1[col-1] + a1
            str0 = str0[:len(str0) - 1]
            str1 = str1[:len(str1) - 1]
        else:
            print("Invalid value in backtrack array")
            return
    return (a0, a1)

def globalScoreTable(a, b, match, mismatch, gap):
    numRows = len(a)+1
    numCols = len(b)+1
    scoringMatrix = [[0]*numCols for _ in range(numRows)]
    scoringMatrix = sideC(scoringMatrix, gap)
    for row in range(1, numRows):
        for col in range(1, numCols):
            up = scoringMatrix[row-1][col] - gap
            left = scoringMatrix[row][col-1] - gap
            diag = scoringMatrix[row-1][col-1] - mismatch
            if a[row-1] == b[col-1]:
                diag += mismatch + match
            scoringMatrix[row][col] = max([up, left, diag])
    return scoringMatrix

def sideC(scoringMatrix, gap):
    for i in range(1, len(scoringMatrix)):
        scoringMatrix[i][0] = -i*gap
    for i in range(1, len(scoringMatrix[0])):
        scoringMatrix[0][i] = -i*gap
    return scoringMatrix

print("ATCGATCGT","ATCGGCTAC", *globalAlignment("ATCGATCGT","ATCGGCTAC", 1, 1, 5), sep="\n")
print("AG", "AT", *globalAlignment("AG","AT", 1, 1, .4), sep="\n")

#LCS Length
def LCSLength(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    scoringMatrix = LCSScoreMatrix(a, b)
    return scoringMatrix[len(a)][len(b)]

def LCSScoreMatrix(a, b):
    numRows = len(a)+1
    numCols = len(b)+1
    scoringMatrix = [[0]*numCols for _ in range(numRows)]
    for row in range (1, numRows):
        for col in range (1, numCols):
            up = scoringMatrix[row-1][col]
            left = scoringMatrix[row][col-1]
            diag = scoringMatrix[row-1][col-1]
            if a[row-1] == b[col-1]:
                diag += 1
            scoringMatrix[row][col] = max([up, left, diag])
    return scoringMatrix

#Longest Common Subsequence
def longestCommonSubsequence(str0, str1):
    backtrack = LCSBacktrack(str0, str1)
    return outputLCS(str0, str1, backtrack)

def outputLCS(str0, str1, backtrack):
    s = ""
    while len(str0) > 0 or len(str1) > 0:
        row = len(str0)
        col = len(str1)
        if backtrack[row][col] == "UP":
            str0 = str0[:len(str0)-1]
        elif backtrack[row][col] == "LEFT":
            str1 = str1[:len(str1)-1]
        elif backtrack[row][col] == "DIAG":
            if str0[len(str0)-1] == str1[len(str1)-1]:
                s = str0[len(str0)-1] + s
            str0 = str0[:len(str0) - 1]
            str1 = str1[:len(str1) - 1]
        else:
            print("Invalid value in backtrack array")
            return
    return s

def LCSBacktrack(str0, str1):
    numRows = len(str0)+1
    numCols = len(str1)+1
    backtrack = [[0]*numCols for _ in range(numRows)]
    scoringMatrix = LCSScoreMatrix(str0, str1)

    for i in range(1, numCols):
        backtrack[0][i] = "LEFT"
    for i in range(1, numRows):
        backtrack[i][0] = "UP"
    for i in range(1, numRows):
        for j in range(1, numCols):
            if scoringMatrix[i][j] == scoringMatrix[i-1][j]:
                backtrack[i][j] = "UP"
            if scoringMatrix[i][j] == scoringMatrix[i][j-1]:
                backtrack[i][j] = "LEFT"
            else:
                backtrack[i][j] = "DIAG"
    return backtrack

#Edit-Distance Matrix
def editDistance(a, b):
    mtx = matches2(a, b)
    return mtx[len(a)][len(b)]

def matches2(a, b):
    numRows = len(a) + 1
    numCols = len(b) + 1
    scoringMatrix = [[0] * numCols for _ in range(numRows)]
    scoringMatrix = sideC2(scoringMatrix)
    for row in range(1, numRows):
        for col in range(1, numCols):
            up = scoringMatrix[row-1][col]+1
            left = scoringMatrix[row][col-1]+1
            diag = scoringMatrix[row-1][col-1]+1
            if a[row - 1] == b[col - 1]:
                diag -= 1
            scoringMatrix[row][col] = min([up, left, diag])
    return scoringMatrix

def sideC2(m):
    for i in range(1, len(m)):
        m[i][0] = i
    for i in range(1, len(m[0])):
        m[0][i] = i
    return m

def editDistanceMatrix(n):
    distanceMatrix = [[0]*len(n) for _ in range(len(n))]
    limit = 0
    for row in range(len(n)):
        for col in range(limit, len(n)):
            if row == col:
                distanceMatrix[row][col] = 0
            else:
                distanceMatrix[row][col] = editDistance(n[row], n[col])
                distanceMatrix[col][row] = distanceMatrix[row][col]
        limit += 1
    return distanceMatrix

#generate list of substrings
def findSubstrings(string):
	substrings = []
	for i in range(1, len(string) + 1):
		for j in range(0, len(string) - i + 1):
			if (string[j:j+i] not in substrings):
				substrings.append(string[j:j+i])
	
	return substrings
	
#find all shared substrings between both lists
def findSharedSubstrings(list1, list2):
	sharedSubstrings = []
	for str1 in list1:
		for str2 in list2:
			if str1 == str2 and str1 not in sharedSubstrings:
				sharedSubstrings.append(str1)
	return sharedSubstrings

#find the longest shared substring from a list of shared substrings
def findLongestShared(list):
	maxLength = 0
	lcs = ""
	for str in list:
		if len(str) > maxLength:
			lcs = str
			maxLength = len(str)
	
	return lcs

#Untranslated Algorithms
'''
func FrequentWords(text string, k int) []string {
	freqPatterns := make([]string, 0)

	freqMap := FrequencyMap(text, k)

	// find the max value of frequency map
	m := MaxMap(freqMap)

	// what achieves the max?
	for pattern, val := range freqMap {
		if val == m {
			// frequent pattern found! append it to our list
			freqPatterns = append(freqPatterns, pattern)
		}
	}

	return freqPatterns
}

//MaxMap returns the maximum value in a frequency map.
func MaxMap(freqMap map[string]int) int {
	m := 0

	// range through map, and if something has higher value, update m!
	for pattern := range freqMap {
		if freqMap[pattern] > m {
			m = freqMap[pattern]
		}
	}
	// if all values in map were negative integers, this would return 0.
	// challenge: fix this bug so that it finds max value of any map of strings to ints.

	return m
}

//FrequencyMap takes a string text and an integer k. It produces a map
//of all k-mers in the string to their number of occurrences.
func FrequencyMap(text string, k int) map[string]int {
	// map declaration is analogous to slices
	// (we don't need to give an initial length)
	freq := make(map[string]int)
	n := len(text)
	for i := 0; i < n-k+1; i++ {
		pattern := text[i : i+k]
		// if freqMap[pattern] doesn't exist, create it.  How do we do this?
		/*
		   // approach #1
		   _, exists := freq[pattern]
		   if exists == false {
		     // create this value
		     freqMap[pattern] = 1
		   } else {
		     // we already have a value in the map
		     freqMap[pattern]++
		   }
		*/
		// approach #2
		// this says, if freqMap[pattern] exists, add one to it
		// if freqMap[pattern] doesn't exist, create it with a default value of 0, and add 1.
		freq[pattern]++
	}
	return freq
}

func PatternCount(pattern, text string) int {
	hits := StartingIndices(pattern, text)
	return len(hits)
}

func StartingIndices(pattern, text string) []int {
	hits := make([]int, 0)

	// append every starting position of pattern that we find in text

	n := len(text)
	k := len(pattern)

	for i := 0; i < n-k+1; i++ {
		if text[i:i+k] == pattern {
			// hit found!
			hits = append(hits, i)
		}
	}

	return hits
}

func SkewArray(genome string) []int {
	n := len(genome)
	array := make([]int, n+1)

	for i := range genome {
		/*
		   array[i+1] = array[i] + something
		   something = -1, 0, 1 depending genome[i]
		*/
		if genome[i] == 'A' || genome[i] == 'T' {
			array[i+1] = array[i]
		} else if genome[i] == 'C' {
			array[i+1] = array[i] - 1
		} else if genome[i] == 'G' {
			array[i+1] = array[i] + 1
		}
	}

	return array
}

func ReverseComplement(text string) string {
	return Reverse(Complement(text))
}

//Reverse takes a string and returns the reversed string.
func Reverse(text string) string {
	n := len(text)
	symbols := make([]byte, n)
	for i := range text {
		symbols[i] = text[n-i-1]
	}
	return string(symbols)
}

func Complement(text string) string {
	// as with arrays, we can use "range"

	n := len(text)
	symbols := make([]byte, n)

	for i := range text {
		if text[i] == 'A' {
			symbols[i] = 'T'
		} else if text[i] == 'T' {
			symbols[i] = 'A'
		} else if text[i] == 'C' {
			symbols[i] = 'G'
		} else if text[i] == 'G' {
			symbols[i] = 'C'
		}
	}

	return string(symbols)
}

func CountSharedKmers(a string, b string, k int) int {
  sum := 0
  akmaps := make(map[string]int)
  bkmaps := make(map[string]int)
  for i := 0; i < len(a) - k + 1; i++ {akmaps[a[i:i+k]]++}
  for i := 0; i < len(b) - k + 1; i++ {bkmaps[b[i:i+k]]++}
  for key := range akmaps {
    if akmaps[key] != 0 {
      if akmaps[key] < bkmaps[key] {
        sum += akmaps[key]
      } else {
        sum += bkmaps[key]
      }
    }
  }
  return sum
}

func LongestSharedSubstring(a, b string) string {
	min := len(a)
	if len(b) < min {
		min = len(b)
	}
	for i := min; i > 0; i-- {
		for in := 0; in < min-i+1; in++ {
			if strings.Contains(b, a[in:i+in]) {
				return a[in : i+in]
			}
		}
	}
	return ""
}

func LocalAlignment(str1, str2 string, match, mismatch, gap float64) (Alignment, int, int, int, int) {
	localAligns := LocalScoreTable(str1, str2, match, mismatch, gap)
	end1, end2 := Max2D(localAligns)
	optAlignment, start1, start2 := PositionFinder(localAligns, end1, end2, match, mismatch, gap, str1, str2)
	return optAlignment, start1, end1, start2, end2
}

func PositionFinder(mtx [][]float64, endRow, endCol int, match, mismatch, gap float64, a, b string) ([2]string, int, int) {
	row := len(mtx) - 1
	col := len(mtx[0]) - 1
	str1 := ""
	str2 := ""
	diag := 0.0
	for row != 0 && col != 0 {
		if a[row-1] == b[col-1] {
			diag = match
		} else {
			diag = -mismatch
		}

		if Max1([]float64{mtx[row-1][col] - gap, mtx[row][col-1] - gap, mtx[row-1][col-1] + diag, 0}) == mtx[row-1][col]-gap {
			str1 = a[row-1:row] + str1
			str2 = "-" + str2
			row--
		} else if Max1([]float64{mtx[row-1][col] - gap, mtx[row][col-1] - gap, mtx[row-1][col-1] + diag, 0}) == mtx[row][col-1]-gap {
			str1 = "-" + str1
			str2 = b[col-1:col] + str2
			col--
		} else if Max1([]float64{mtx[row-1][col] - gap, mtx[row][col-1] - gap, mtx[row-1][col-1] + diag, 0}) == mtx[row-1][col-1]+diag {
			str1 = a[row-1:row] + str1
			str2 = b[col-1:col] + str2
			row--
			col--
		} else if Max1([]float64{mtx[row-1][col] - gap, mtx[row][col-1] - gap, mtx[row-1][col-1] + diag, 0}) == 0 {
			break
		}
	}
	alignment := [2]string{str1, str2}
	return alignment, row, col
}

func Max2D(mtx [][]float64) (int, int) {
	max := mtx[0][0]
	endRow := 0
	endCol := 0
	for i := 0; i < len(mtx); i++ {
		for j := 0; j < len(mtx[0]); j++ {
			if mtx[i][j] > max {
				max = mtx[i][j]
			}
			endRow = i
			endCol = j
		}
	}
	return endRow, endCol
}

func LocalScoreTable(str1, str2 string, match, mismatch, gap float64) [][]float64 {
	numRows := len(str1) + 1
	numCols := len(str2) + 1
	scoringMatrix := make([][]float64, numRows)
	for i := range scoringMatrix {
		scoringMatrix[i] = make([]float64, numCols)
	}
	up := 0.0
	left := 0.0
	diag := 0.0
	for row := 1; row < numRows; row++ {
		for col := 1; col < numCols; col++ {
			up = scoringMatrix[row-1][col] - gap
			left = scoringMatrix[row][col-1] - gap
			diag = scoringMatrix[row-1][col-1] - mismatch
			if str1[row-1] == str2[col-1] {
				diag += mismatch + match
			}
			scoringMatrix[row][col] = Max1([]float64{up, left, diag, 0})
			// if row == len(str1) && col == len(str2) {
			// 	maxSink := scoringMatrix[0][0]
			// 	for i := 0; i <= len(str1); i++ {
			// 		for j := 0; j <= len(str2); j++ {
			// 			if scoringMatrix[i][j] > maxSink {
			// 				maxSink = scoringMatrix[i][j]
			// 			}
			// 		}
			// 	}
			// 	scoringMatrix[row][col] = maxSink
			// }
		}
	}
	return scoringMatrix
}


'''
