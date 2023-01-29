import boto3
from botocore.exceptions import ClientError
import os


def upload_files(data):
    try:
        result = []
        if type(data) == list:
            for file in data:
                menuResult = upload_file(file["menuPath"], f'{file["storeId"]}_menu')
                optionResult = upload_file(file["optionFilePath"], f'{file["storeId"]}_options')
                result.append(menuResult)
                result.append(optionResult)
        return result
    except RuntimeError as e:
        print('Upload file error')
        return [False]

def upload_file(file_name, object_name=None):
    bucket = os.getenv('BUCKET_NAME')
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, f'{object_name}.csv')
    except ClientError as e:
        return False
    return True