import json
import excel2json
import time
import uuid

from datetime import datetime
from decimal import Decimal
from dynamodb_json import json_util as json

class Dynamo_Upload:
# --------- Launch Convert and upload App --------- #

    def __init__(self,file):
        print("Launch File Convert & Dynamo Upload App")
        print("Converting file %s" % file)

        self.Convert2Dynamodb(file)

        #self.AWSUpload(file)

# --------- Convert File --------- #

    def Convert_Exel2Json(self,file):
        print("convert json to dynamo json")
        file = str(file)
        excel2json.convert_from_file(file)

    def Convert_XML2Json(self,file,newName):
        with open(file, 'r') as f:
            data = f.read()
            newdata = dumps(bf.data(fromstring(data)))

        with open(newName, 'w+') as n:
            n.write(newdata)
        print("ok" , input ," has been converted to ", newName, flush=True)

    def Convert_CSV2Json(self,file):
        print("test")

# --------- Convert to Dynamo json and Choose file --------- #

    def Convert2Dynamodb(self,file):
        with open(file ,"r") as json_file:
            json_ = json_file.read()
            obj = json.loads(json_)
            dynamodb_json = json.dumps(obj)
            json_file.close()

        with open(file, "w+") as outfile:
            outfile.write(dynamodb_json)
            print(dynamodb_json)

    def Choose_files(self,FileDir):
        list=[]
        entry = os.listdir(FileDir)
        for i in entry:
            if i.endswith('.xml'):
                list.append(i)
            if i.endswith('.xlsx'):
                list.append(i)
            if i.endswith('.csv'):
                list.append(i)
            if i.endswith('.json'):
                list.append(i)

        input = list[0]
        input = str(input)
        name, ext = os.path.splitext(input)
        ext = str(ext)
        newName = str(name+".json")

        if ext ==".xlsx":
            self.Convert_Exel2Json(input)
        if ext ==".csv":
            self.Convert_CSV2Json(input)
        if ext ==".xml":
            self.XML2Json(input,newName)
        if ext =="json":
            self.Convert2Dynamodb(input)

# --------- send to AWS --------- #
    def AWSUpload(self,file):
        print("Uploading %s to Dynamodb" % file)

if __name__ == "__main__":

    Dynamo_Upload("new.json")
