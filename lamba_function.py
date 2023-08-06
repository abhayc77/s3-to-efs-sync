import json
import os
import io
import json
import boto3
from urllib.parse import unquote_plus


def lambda_handler(event, context):
    print("In Lambda.. starting sync.. ")
    EFS_PATH = "/mnt/s3-sync"
    if event:
        print("Event found")
        print(event)
        file_obj = event["Records"][0]
         # fetching bucket name from event
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        # fetching file name from event
        filename = unquote_plus(str(file_obj["s3"]["object"]["key"]))
        print("Bucket name: ", bucketname, ", FileName: ",filename)
        s3 = boto3.client("s3")
        print("S3 client initialized:")
        # retrieving object from S3
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        print("File reading from s3 successful")
        # reading botocore stream
        file_content = fileObj["Body"].read()
        data_buf = io.BytesIO(file_content)
        print("Got data buffer")
        folder_name = EFS_PATH+"/"+bucketname
        print("checking and creating folder",folder_name)

        if not os.path.exists(folder_name):
            print("Folder ",folder_name, " does not exist.. creating the folder")
            # if the folder_name directory is not present then create it.
            os.makedirs(folder_name)
            print("Created Folder: ",folder_name)
        else:
            print("Folder ",folder_name, "already exists")

        print("Before Sync: ",os.listdir(folder_name+"/"))
        dstFileName = folder_name+"/"+filename
        print("Writing to file: ", dstFileName)
        with open(dstFileName,"wb") as f:
            f.write(data_buf.getbuffer())
        l = os.listdir(EFS_PATH)
        print("After Sync: ",l)
    else:
        print("Event not found!!")