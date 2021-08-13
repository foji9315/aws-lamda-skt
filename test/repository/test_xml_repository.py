import os

from src.repository.xml_repository import upload_xml
import test.test_utils.constants as constants


def test_upload_xml_name(s3_test):
    url_resource = upload_xml('xml-content', constants.BUCKET_NAME)
    expected_url = 'https://{}.s3.{}.amazonaws.com/{}'.format(constants.BUCKET_NAME,
                                                              constants.DEFAULT_AWS_REGION,
                                                              constants.DEFAULT_FILE_NAME)
    assert url_resource != ''
    assert url_resource == expected_url


def test_upload_xml_happy_path(s3_test):
    os.environ["AWS_REGION"] = "us-east-1"
    url_resource = upload_xml('xml-content', constants.BUCKET_NAME, "name_file.xml")
    expected_url = 'https://{}.s3.{}.amazonaws.com/{}'.format(constants.BUCKET_NAME,
                                                              os.environ["AWS_REGION"],
                                                              "name_file.xml")
    assert url_resource != ''
    assert url_resource == expected_url
