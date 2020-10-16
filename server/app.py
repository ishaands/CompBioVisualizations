from flask import Flask, request
from server.examples import hamming
from server.other import helper

app = Flask(__name__)

#test lol
@app.route('/')
def hello_world():
    return "Welcome to the Server!"

@app.route('/hamming', methods=['POST'])
def returnStrings():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")
    return hamming.hamming(str1, str2)
    



    
