import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def upload_xml(xml_text, bucket_name, object_name=None):
    if object_name is None:
        object_name = "reservation.xml"
    try:
        client = boto3.client('s3')
        logger.info("Client meta %s", client.meta)

        response = client.put_object(Body=xml_text, Bucket=bucket_name, Key=object_name, ACL='public-read')
        logger.info("response from bucket %s", response)

        return True, 'https://{}.s3.{}.amazonaws.com/{}'.format(bucket_name, "us-east-2", object_name)

    except ClientError as e:
        logging.error(e)
        return False, 'error Uploading file'
