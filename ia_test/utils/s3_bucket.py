import boto3
import os
from app.config import AWS_ACCOUNT_ID, AWS_BUCKET_NAME


class S3Bucket:
    def __init__(self, acl='private', location=''):
        self.acccount_id = AWS_ACCOUNT_ID
        self.bucket = AWS_BUCKET_NAME
        self.acl = acl
        self.location = location
        self.client = self.get_client()
        self.get_bucket()
        self.bucket_url = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com"

    def get_client(self):
        return boto3.client('s3')

    def is_bucket_exits(self):
        response = self.client.list_buckets()
        list_buckets = response.get('Buckets', [])

        is_bucket_exits = list(filter(lambda bucket: bucket.get('Name') == self.bucket, list_buckets))
        return is_bucket_exits

    def get_bucket(self):
        try:
            if not self.is_bucket_exits():
                self.client.create_bucket(ACL=self.acl, Bucket=self.bucket)
            else:
                print(f'El bucket {self.bucket} ya existe')
        except Exception as err:
            print(err)

    def upload_file(self, path='', filename=''):
        self.client.upload_file(path, self.bucket, filename)

    def upload_file_public(self, path="", directory="", filename="", type=""):
        try:
            bucket_filename = f"{directory}/{filename}"
            self.client.upload_file(path, self.bucket, bucket_filename, ExtraArgs={"ACL": "public-read", "ContentType": type})
            return f"{self.bucket_url}/{bucket_filename}"
        except Exception:
            return False

    def download_file(self, key='', filename='.'):
        paths = filename.split('/')
        directory = list(filter(lambda path: ".zip" not in path, paths))
        directory = directory[0]

        if not os.path.isdir(directory):
            os.mkdir(directory)

        self.client.download_file(self.bucket, key, filename)

    def list_objects(self):
        response = self.client.list_objects(Bucket=self.bucket)
        return response.get('Contents')

    def delete_bucket(self):
        try:
            if self.is_bucket_exits():
                self.client.delete_bucket(Bucket=self.bucket, ExpectedBucketOwner=self.acccount_id)
        except Exception as err:
            print(err)
            
    def delete_file_bucket(self, filename=''):
        try:
            response = self.client.delete_object(Bucket=self.bucket, Key=filename)
            print("delete_file_bucket", response)
            
        except Exception as err:
            print(err)
            
    def get_objectfile_bucket(self, filename=''):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=filename)
            print("get_objectfile_bucket", response)
            
        except Exception as err:
            print(err)
