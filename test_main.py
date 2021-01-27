from main import get_client, list_buckets, create_bucket
from botocore.stub import Stubber
import datetime


def test_get_client():
    s3 = get_client()


def test_create_bucket():
    s3 = get_client()

    method = "create_bucket"
    response = {"Location": "string"}
    params = {"Bucket": "stubberbucket1"}

    with Stubber(s3) as stubber:
        stubber.add_response(method, response, params)
        service_response = s3.create_bucket(Bucket="stubberbucket1")

    assert service_response == response


def test_list_buckets():
    s3 = get_client()

    method = "list_buckets"
    response = {
        "Buckets": [
            {"Name": "stubberbucket1", "CreationDate": datetime.datetime(2020, 1, 1)},
        ],
        "Owner": {"DisplayName": "Test", "ID": "Stubber"},
    }
    params = {}

    with Stubber(s3) as stubber:
        stubber.add_response(method, response, params)
        service_response = s3.list_buckets()

        assert service_response == response


# def test_call_everything():

#     call_everything()
