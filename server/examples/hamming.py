
def hamming(str1, str2):
    if (len(str1) != len(str2)):
        return {"exit-code": "1"}

    match = ""
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            match += "-"
        else:
            match += "+"
            
    
    return {"match-sequence" : match}