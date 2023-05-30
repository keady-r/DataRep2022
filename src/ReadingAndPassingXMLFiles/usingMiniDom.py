## reading and passing files through xml

from xml.dom.minidom import parse
filename = input("please choose which file to output: Books.xml, Breakfast.xml, or employees.xml :   ")

#read files in two ways

doc = parse(filename)

#or
with open (filename) as fp:
    doc = parse(fp)

print(doc.toprettyxml(), end ='')
