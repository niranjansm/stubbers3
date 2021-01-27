import boto3
from botocore.stub import Stubber
import datetime

FILE_NAME = "hello.txt"

def get_client():

    return boto3.client("s3", region_name="us-east-1")


def create_bucket(s3_client, bucket_name):

    s3_client.create_bucket(Bucket=bucket_name)


# def delete_bucket(s3_client, bucket_name):

#     s3_client.delete_bucket(Bucket=bucket_name)

def list_buckets(s3_client):

    list_response = s3_client.list_buckets()
    buckets = list_response.get("Buckets")

    bucket_names = [bucket['Name'] for bucket in buckets]

    return bucket_names

# def upload_file(s3_client, bucket_name):

#     s3_client.upload_file('./' + FILE_NAME, bucket_name, FILE_NAME)

# def download_file(s3_client, bucket_name):

#     s3_client.download_file(bucket_name, FILE_NAME, 'downloaded' + FILE_NAME)

# def delete_object(s3_client, bucket_name):

#     s3_client.delete_object(Bucket=bucket_name, Key=FILE_NAME)

# def list_bucket_objects(s3_client, bucket_name):

#     objects = []
#     try:
#         contents = s3_client.list_objects(Bucket=bucket_name)['Contents']
#         for item in contents:
#             objects.append(item.get("Key"))
#     except KeyError:
#         pass

#     print(f"Bucket: {bucket_name}\t Objects: {objects}")
#     return objects

def call_everything():
    s3 = get_client()

    # Create 2 mock buckets
    create_bucket(s3, "mockbucket1")
    create_bucket(s3, "mockbucket2")
    create_bucket(s3, "mockbucket3")

    # List all the bucket names
    print("\n##### After bucket creation #####")
    bucket_names = list_buckets(s3)
    print(f"Buckets Created :{bucket_names}")

    # Upload a file to both the buckets
    for bucket in bucket_names:
        upload_file(s3, bucket)

    # Download a file from one of the buckets
    myfile = download_file(s3, bucket_names[0])

    # List ojects in all the buckets
    print("\n##### After object creation #####")
    for bucket in bucket_names:
        objects = list_bucket_objects(s3, bucket)

    # Delete file from one of the buckets
    delete_object(s3, bucket_names[0])

    # List ojects in all the buckets after deletion of objects
    print("\n##### After object deletion #####")
    for bucket in bucket_names:
        objects = list_bucket_objects(s3, bucket)

    delete_bucket(s3, bucket_names[0])

    # List ojects in all the buckets after deleting a bucket
    print("\n##### After bucket deletion #####")
    # Refresh the bucket list
    bucket_names = list_buckets(s3)

    for bucket in bucket_names:
        objects = list_bucket_objects(s3, bucket)

# if __name__ == "__main__":

#     test = False
#     # if test == True:
#     #     mock = mock_s3()
#     #     mock.start()
#     with mock_s3():
#      call_everything()

#     # if test == True:
#     #     mock.stop()
