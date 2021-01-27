from main import (
    get_client,
    list_buckets,
    create_bucket,
    upload_file,
    list_bucket_objects,
)
from botocore.stub import Stubber
import datetime


def test_get_client():
    s3 = get_client()


# def test_create_bucket():
#     s3 = get_client()

#     method = "create_bucket"
#     response = {"Location": "eu-west-1"}
#     params = {"Bucket": "stubberbucket1"}
#     bucket_name = "stubbertest"

#     with Stubber(s3) as stubber:
#         stubber.add_response(method, response, params)
#         service_response = create_bucket(s3, "stubbertest")

#     assert service_response == response


def test_list_buckets():
    s3 = get_client()

    bucketlist = ["stubberbucket1", "stubberbucket2"]
    list_bucket_response = {
        "Buckets": [
            {"Name": "stubberbucket1", "CreationDate": datetime.datetime(2020, 1, 1)},
            {"Name": "stubberbucket2", "CreationDate": datetime.datetime(2020, 1, 1)},
        ],
        "Owner": {"DisplayName": "Test", "ID": "Stubber"},
    }

    with Stubber(s3) as stubber:
        stubber.add_response("create_bucket", {}, {"Bucket": bucketlist[0]})
        create_bucket(s3, bucketlist[0])

        stubber.add_response("create_bucket", {}, {"Bucket": bucketlist[1]})
        create_bucket(s3, bucketlist[1])

        stubber.add_response("list_buckets", list_bucket_response, {})
        service_response = list_buckets(s3)

        assert bucketlist == service_response


def test_upload_file():
    s3 = get_client()

    bucket_name = "uploadbucket"
    # response = {
    #     "Buckets": [
    #         {"Name": "stubberbucket1", "CreationDate": datetime.datetime(2020, 1, 1)},
    #     ],
    #     "Owner": {"DisplayName": "Test", "ID": "Stubber"},
    # }

    with Stubber(s3) as stubber:
        stubber.add_response("create_bucket", {}, {"Bucket": bucket_name})
        create_bucket(s3, bucket_name)

        # stubber.add_response("upload_file", {}, {})
        # upload_file(s3, bucket_name)

        list_objects_response = {
            "ResponseMetadata": {
                "HTTPStatusCode": 200,
                "HTTPHeaders": {},
                "RetryAttempts": 0,
            },
            "IsTruncated": False,
            "Contents": [
                {
                    "Key": "hello.txt",
                    "LastModified": datetime.datetime(2021, 1, 27, 21, 6),
                    "ETag": '"931e2b237e0d22bd1401365c0d0668f8"',
                    "Size": 28,
                    "StorageClass": "STANDARD",
                    "Owner": {
                        "DisplayName": "webfile",
                        "ID": "75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a",
                    },
                }
            ],
            "Name": "uploadbucket",
            "Delimiter": "None",
            "MaxKeys": 1000,
        }

        stubber.add_response(
            "list_objects", list_objects_response, {"Bucket": bucket_name}
        )
        objects = list_bucket_objects(s3, bucket_name)

        assert objects == ["hello.txt"]


# def test_call_everything():

#     call_everything()
