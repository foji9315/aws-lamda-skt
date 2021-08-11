import boto3
import os
import pytest

from moto import mock_s3
import test.test_utils.constants as constants


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ['BUCKET_NAME'] = constants.BUCKET_NAME


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = boto3.client("s3", region_name="us-east-1")
        yield conn


@pytest.fixture
def bucket_name():
    return constants.BUCKET_NAME


@pytest.fixture
def s3_test(s3_client, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name)
    yield


@pytest.fixture
def json_input():
    return open('test/files/input.json', 'r').read()
