from xmljson import yahoo as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import json
import os

list=[]
entry = os.listdir('/Users/Q/MAC-Repo/Code/Python/PythonApps')
for i in entry:
    if i.endswith('.xml'):
        list.append(i)

input = list[0]
input = str(input)
name, ext = os.path.splitext(input)
ext = str(ext)
newName = str(name+".json")

def XML2Json(file):
    with open(file, 'r') as f:
        data = f.read()
        newdata = dumps(bf.data(fromstring(data)))
    with open(newName, 'w+') as n:
        n.write(newdata)
    print("ok" , input ," has been converted to ", newName, flush=True)

if __name__ == "__main__":

    if ext ==".xml":
        XML2Json(input)
        os.remove(list[0])
        list.remove(input)

    else:
        print("invalid input, input XML format")
