import json
import os
import io
import json
import boto3
from urllib.parse import unquote_plus


def lambda_handler(event, context):
    print("In Lambda.. starting sync.. ")
    EFS_PATH = "/mnt/s3-sync2/"
    if event:
        print("Event found")
        print(event)
        file_obj = event["Records"][0]
         # fetching bucket name from event
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        # fetching file name from event
        filename = unquote_plus(str(file_obj["s3"]["object"]["key"]))
        print("Bucket name: ", bucketname, ", FileName: ",filename)
        print("Before Sync: ",os.listdir(EFS_PATH))
        s3 = boto3.client("s3")
        print("S3 client initialized:")
        # retrieving object from S3
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        print("File reading from s3 successful")
        # reading botocore stream
        file_content = fileObj["Body"].read()
        data_buf = io.BytesIO(file_content)
        print("Got data buffer")
        dstFileName = EFS_PATH+filename
        print("Writing to file: ", dstFileName)
        with open(dstFileName,"wb") as f:
            f.write(data_buf.getbuffer())
        l = os.listdir(EFS_PATH)
        print("After Sync: ",l)
    else:
        print("Event not found!!")