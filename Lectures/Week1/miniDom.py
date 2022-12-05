##THere are two options for reading and passing files through xml

#OPTION_1
#For files

from xml.dom.minidom import parse
filename = "employees.xml"

#read files in two ways

doc = parse(filename)

#or
with open (filename) as fp:
    doc = parse(fp)

print(doc.toprettyxml(), end ='')


#OPTION_2 
#for content from the cloud

import requests

from xml.dom.minidom import parseString

url = "https://www.google.com/search?q=how+to+screenshot+on+mac&oq=how+to+scre&aqs=chrome.3.0i131i433i512j0i512j69i57j0i512l7.3855j0j7&sourceid=chrome&ie=UTF-8"

page = requests.get(url)
doc = parseString(page.content)

print (doc.toprettyxml(), end ='')

#LAB
from xml.dom.minidom import parse

filename = "employees.xml"

# read file in two ways
doc = parse(filename)
# or
#with open(filename) as fp:
#    doc = parse(fp)

emloyeeNodeList = doc.getElementsByTagName("Employee")
print(len(emloyeeNodeList))
for employeeNode in emloyeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print (firstName)

#END
