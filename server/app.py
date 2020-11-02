from flask import Flask, request
from server.examples import hamming
from server.metagenomics import meta
from server.alignment import alignment
from server.other import helper

app = Flask(__name__)

def checkNull(obj1):
    if (obj1 is None):
        print("term " + obj1 + " is null")
        return True
    
    return False

#welcome screen for server
@app.route('/')
def hello_world():
    return "Welcome to the Server!"

#return json for hamming distance of two strings
@app.route('/hamming', methods=['POST'])
def returnStrings():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    #check validity of parameters
    str1 = dict["str1"]
    str2 = dict["str2"]
    if (checkNull(str1) or checkNull(str2)): return {"exit-code" : 1}
    #return match sequence of +/- in json format
    matchsequence = hamming.hamming(str1, str2)

    return matchsequence

#return json of jaccard distance between two metagenomic samples
@app.route('/jaccard', methods=['POST'])
def getJaccard():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    #check validity of parameters

    dict1 = dict["dict1"]
    dict2 = dict["dict2"]
    if (checkNull(dict1) or checkNull(dict2)): return {"exit-code" : 1}

    returninfo = meta.jaccardDistance(dict1, dict2)

    return returninfo

#return json of bray curtis distnace for two metagenomic samples
@app.route('/bray-curtis', methods=['POST'])
def getBrayCurtis():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    
    #check validity of parameters
    dict1 = dict["dict1"]
    dict2 = dict["dict2"]
    if (checkNull(dict1) or checkNull(dict2)): return {"exit-code" : 1}

    returninfo = meta.brayCurtisDistance(dict1, dict2)

    return returninfo

#find all substrings of a string
@app.route('/lss-findsubstrings', methods=['POST'])
def getSubstrings():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    
    #check validity of parameters
    str1 = dict["str1"]
    str2 = dict["str2"]
    if (checkNull(str1) or checkNull(str2)): return {"exit-code" : 1}

    #find all substrings for each of the strings for longest shared substring
    substrings1 = alignment.findSubstrings(str1)
    substrings2 = alignment.findSubstrings(str2)

    return {"str1" : substrings1, "str2" : substrings2}

#find shared strings between two lists
@app.route('/lss-findshared', methods = ['POST'])
def getShared():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    
    #check validity of parameters
    list1 = dict["list1"]
    list2 = dict["list2"]
    if (checkNull(list1) or checkNull(list2)): return {"exit-code" : 1}

    sharedSubstrings = alignment.findSharedSubstrings(list1, list2)

    return {"shared-substrings" : sharedSubstrings}

#find longest string in a list of strings
@app.route('/lss', methods = ['POST'])
def longestSharedSubstring():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}

    #check validity of parameters
    list = dict["list"]
    if (checkNull(list)): return {"exit-code" : 1}

    lcs = alignment.findLongestShared(list)

    return {"longest-shared-substring" : lcs}

#dp algorithm visualization return for edit distance
@app.route('/dptest', methods = ['POST'])
def getEditDistance():
    #get input from json
    dict = request.get_json()
    if checkNull(dict): return {"exit-code" : 1}
    
    #check validity of parameters
    str1 = dict["str1"]
    str2 = dict["str2"]
    if (checkNull(str1) or checkNull(str2)): return {"exit-code" : 1}

    returnedInfo = alignment.editDistance(str1, str2)

    return returnedInfo

    