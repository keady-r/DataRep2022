from flask import Flask, url_for, request, redirect, abort


app = Flask(__name__, static_url_path='', static_folder='staticpages' )

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    return "served by login"

@app.route('/user')
def getUser():
    return "served by get user"

@app.route('/user/<int:id>')
def findUserbyID(id):
    return "served by finsUserby ID"+str(id) 

@app.route('/user/<int:id>', methods =['POST'])
def createUser():
    return "served by create user"

@app.route('/demo_url_for')
def demoUrlFor():
    returnString = "url for index is" +url_for('index')
    returnString += "<br/>" 
    returnString = "url for findUserByID" +url_for('findUserByID')
    return returnString

@app.route("/demo_request", methods =['POST', 'GET','DELETE'])
def demoRequest():
    return request.method

if __name__ =="__main__":
    print("in_if")
    app.run(debug = True)