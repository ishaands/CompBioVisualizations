# Convert DNA to RNA
def DNAToRNA(genome):
    rna = ""

    for char in genome:
        if char == "T":
            rna += "U"
        elif char == "A" or char == 'G' or char == 'C':
            rna += char
        else:
            raise ValueError("Characters in genome should only be A, T, G, or C. The value of the character was " + char)
    return rna


# Open Reading Frames (Area of codons that starts with a start codon and ends with a stop codon)
class ORF:
    def __init__(self, startingPosition, length, revComp):
        self.startingPosition = startingPosition
        self.length = length
        self.revComp = revComp



# Translate from rna to amino acid chain
def Translate(rnaStrand, startIndex):
    if rnaStrand[startIndex:startIndex + 3] != "AUG":
        return ""

    aaseq = ""
    # codons_table is a map of strings to strings that maps
    # RNA codons to single amino acids according to the genetic code.

    codons_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UAU": "Y", "UAC": "Y", "UAA": "x", "UAG": "x",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "UGU": "C", "UGC": "C", "UGA": "x", "UGG": "W",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }
    length = len(rnaStrand)

    for i in range(startIndex, length - 3 + 1, 3):
        aa = codons_table[rnaStrand[i:i + 3]]
        if aa == "x":
            return aaseq
        else:
            aaseq += aa

    return ""


# Write open reading frames in specified outfile
def WriteORFsToFile(outFilename, orfs):
    outFile = open(outFilename, "w")

    for i in orfs:
        outFile.write(i.startingPosition + " " + str(i.startingPosition + orfs[i].length))
        if i.revComp:
            outFile.write(" -")
        else:
            outFile.write(" +")

        outFile.write("\n")

    outFile.close()


def FindORFsRNA(rnaStrand, minORFLength, rc):
    if minORFLength <= 0:
        print("Error: minimum ORF length is nonpositive in FindORFsRNA function.")
        return

    orfs = []  # every time we find an ORF we will append it

    # let's make a map to see if we have encountered the index of a given STOP codon before
    stopCodons = {}  # keys are positions of stop codons, values are position of earliest start codon for this ORF

    # ranging through every possible start index and adding any ORF we find to our slice

    for startIndex in range(len(rnaStrand) - minORFLength + 1 - 3):
        readingFrame = Translate(rnaStrand, startIndex)

        orfLength = len(readingFrame) * 3
        if orfLength >= minORFLength:
            # difference from previous function is that we only want to create an ORF
            # if we haven't seen the current stop codon before

            # we will use the stopCodons map to ask, "have I seen this stop codon before?"
            stopIndex = startIndex + orfLength
            if not stopIndex in stopCodons:
                # create an entry in the stopIndex map for this start index
                stopCodons[stopIndex] = startIndex

                # also create my ORF here
                o = ORF(startIndex, orfLength, rc)
                # now append our new ORF to our growing list
                orfs.append(o)
    return orfs




