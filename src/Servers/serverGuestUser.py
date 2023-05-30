from flask import Flask, url_for


app = Flask(__name__, static_url_path='', static_folder='staticpages' )
@app.route('/')
def index():
    return "<a href="+url_for('getuser')+">getuser</a>"

@app.route('/user', methods =['GET'])
def getuser():
    return "Hi there" 
@app.route('/user/<int:id>', methods =['GET'])
def getuserbyid(id):
    return "get user by id"+str(id)
@app.route('/user', methods =['POST'])
def postuser():
    return "in post"

if __name__ =="__main__":
    app.run(debug = True)