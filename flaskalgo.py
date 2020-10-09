from flask import Flask, request

app = Flask(__name__)

#test lol
@app.route('/helloworld')
def hello_world():
    return "Hello World"

@app.route('/hamming', methods=['GET'])
def returnStrings():
    str1 = request.args.get('string 1', None)
    str2 = request.args.get('string 2', None)
    if (len(str1) != len(str2)):
        return {"exit code": "1"}

    match = ""
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            match += "-"
        else:
            match += "+"
    
    return {"match sequence" : match}
