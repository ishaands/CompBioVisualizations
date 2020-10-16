from flask import Flask, request
from ..Algorithms import helper
app = Flask(__name__)

#test lol
@app.route('/')
def hello_world():
    return "Welcome to the Server!"

@app.route('/hamming', methods=['POST'])
def returnStrings():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")
    if (len(str1) != len(str2)):
        return {"exit-code": "1"}

    match = ""
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            match += "-"
        else:
            match += "+"
            
    
    return {"match-sequence" : match}

@app.route('/jaccard', methods=['POST'])
def returnJaccard():
    arr1 = request.args.get("arr1")
    arr2 = request.args.get("arr2")

    

    