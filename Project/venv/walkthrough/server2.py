from flask import Flask, url_for, request, redirect, abort,jsonify


app = Flask(__name__, static_url_path='', static_folder='staticpages' )

books = [
    {"id":1,"Title":"HP", "Author":"JK", "Price":1000},
    {"id":3,"Title":"Ruth", "Author":"rK", "Price":40},
    {"id":4,"Title":"K", "Author":"jK", "Price":190},
    {"id":5,"Title":"Rory", "Author":"kK", "Price":10},
    {"id":6,"Title":"K", "Author":"lK", "Price":100},
    {"id":7,"Title":"Emma k", "Author":"pK", "Price":1700}
]
nextId=8

@app.route('/')
def index():
    return 'hello'

@app.route('/books')
def getAll():
    return jsonify(books)

@app.route('/books/<int:id>')
def findID(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])

    return "find by ID"+str(id)

#curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\",\"Author\":\"Ruth\",\"Price\":15}" http://127.0.0.1:5000/books
@app.route('/books', methods = ['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
        
    book={
        "id": nextId, 
        "Tile": request.json["Title"],
        "Author":request.json["Author"],
        "Price": request.json["Price"],
    }
    books.append(book)
    nextId +=1
    return jsonify(book)

    
#curl -X PUT -d "{\"Title\":\"newtest\",\"Author\":\"newRuth\",\"Price\":4415}" -H "content-type:application/json" http://127.0.0.1:5000/books/4
@app.route('/books/<int:id>', methods = ['PUT'])
def update(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBooks = foundBooks[0]
    
    if "Title" in request.json:
        currentBooks['Title'] = request.json['Title']
        
    if "Author" in request.json:
        currentBooks['Author'] = request.json['Author']
        
    if "Price" in request.json:
        currentBooks['Price'] = request.json['Price']
        
    return jsonify(currentBooks)
#curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods = ['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})

if __name__ =="__main__":
    app.run(debug = True)