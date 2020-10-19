from flask import Flask, request
from server.examples import hamming
from server.metagenomics import meta
from server.alignment import alignment
from server.other import helper

app = Flask(__name__)

#welcome screen for server
@app.route('/')
def hello_world():
    return "Welcome to the Server!"

#return json for hamming distance of two strings
@app.route('/hamming', methods=['POST'])
def returnStrings():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")
    matchsequence = hamming.hamming(str1, str2)
    return matchsequence

#return json of jaccard distance between two metagenomic samples
@app.route('/jaccard', methods=['POST'])
def getJaccard():
    dict1 = request.args.get("dict1")
    dict2 = request.args.get("dict2")

    returninfo = meta.jaccardDistance(dict1, dict2)

    return returninfo

#return json of bray curtis distnace for two metagenomic samples    
@app.route('/bray-curtis', methods=['POST'])
def getBrayCurtis():
    dict1 = request.args.get("dict1")
    dict2 = request.args.get("dict2")

    returninfo = meta.brayCurtisDistance(dict1, dict2)

    return returninfo

@app.route('/lss-findsubstrings', methods=['POST'])
def getSubstrings():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")

    substrings1 = alignment.findSubstrings(str1)
    substrings2 = alignment.findSubstrings(str2)

    return {"str1" : substrings1, "str2" : substrings2}

@app.route('/lss-findshared', methods = ['POST'])
def getShared():
    list1 = request.args.get("list1")
    list2 = request.args.get("list2") 

    sharedSubstrings = alignment.findSharedSubstrings(list1, list2)

    return {"shared-substrings" : sharedSubstrings}



@app.route('/lss', methods = ['POST'])
def longestSharedSubstring():
    list = request.args.get("list")

    lcs = alignment.findLongestShared(list)

    return {"longest-shared-substring" : lcs}
