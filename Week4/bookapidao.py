import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getBookById (id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    book= {
        'Author':"Ruths test", 
        'Title':"Ruths test title",
        "Price":1234
    }
    response = requests.post(url,json=book)
    #Manual Way - headers ={"Content-type":"application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    return response.json()


def updateBook (id, bookdiff):
    updateurl = url + "/"+ str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    book= {
        'Author':"Ruths test", 
        'Title':"Ruths test title",
        "Price":1234
    }
    bookdiff ={
        "Price": 1000000
    }
    #print(getallbooks())
    #print(getBookById(2))
    #print(deleteBook(2))
    #print(createBook(99))
    print(updateBook(242, bookdiff))
    
    #check the status code. when writing for real