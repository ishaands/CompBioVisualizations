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
    #get input from json
    dict = request.get_json()
    str1 = dict["str1"]
    str2 = dict["str2"]
    #return match sequence of +/- in json format
    matchsequence = hamming.hamming(str1, str2)

    return matchsequence

#return json of jaccard distance between two metagenomic samples
@app.route('/jaccard', methods=['POST'])
def getJaccard():
    #get input from json
    dict = request.get_json()
    dict1 = dict["dict1"]
    dict2 = dict["dict2"]

    returninfo = meta.jaccardDistance(dict1, dict2)

    return returninfo

#return json of bray curtis distnace for two metagenomic samples    
@app.route('/bray-curtis', methods=['POST'])
def getBrayCurtis():
    #get input from json
    dict = request.get_json()
    dict1 = dict["dict1"]
    dict2 = dict["dict2"]

    returninfo = meta.brayCurtisDistance(dict1, dict2)

    return returninfo

#find all substrings of a string
@app.route('/lss-findsubstrings', methods=['POST'])
def getSubstrings():
    #get input from json
    dict = request.get_json()
    str1 = dict["str1"]
    str2 = dict["str2"]

    #find all substrings for each of the strings for longest shared substring
    substrings1 = alignment.findSubstrings(str1)
    substrings2 = alignment.findSubstrings(str2)

    return {"str1" : substrings1, "str2" : substrings2}

#find shared strings between two lists
@app.route('/lss-findshared', methods = ['POST'])
def getShared():
    #get input from json
    dict = request.get_json()
    list1 = dict["list1"]
    list2 = dict["list2"]

    sharedSubstrings = alignment.findSharedSubstrings(list1, list2)

    return {"shared-substrings" : sharedSubstrings}

#find longest string in a list of strings
@app.route('/lss', methods = ['POST'])
def longestSharedSubstring():
    #get input from json
    dict = request.get_json()
    list = dict["list"]

    lcs = alignment.findLongestShared(list)

    return {"longest-shared-substring" : lcs}
