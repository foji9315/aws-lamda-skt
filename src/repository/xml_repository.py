import os
import boto3

from src.config.loggerconf import logger


def upload_xml(xml_text, bucket_name, object_name=None):
    if object_name is None:
        object_name = "reservation.xml"

    client = boto3.client('s3')
    logger.info("Client meta {}".format(client.meta))

    response = client.put_object(Body=xml_text, Bucket=bucket_name, Key=object_name, ACL='public-read')
    logger.info("response from bucket {}".format(response))

    return 'https://{}.s3.{}.amazonaws.com/{}'.format(bucket_name, get_region(), object_name)


def get_region():
    if 'AWS_REGION' in os.environ:
        return os.environ['AWS_REGION']
    return "us-east-2"
