import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def uploadXML(xmlText, bucketName, objectName=None):
    if objectName is None:
        objectName = "reservation.xml"
    try:
        client = boto3.client('s3')
        logger.info("Client meta %s", client.meta)

        response = client.put_object(Body=xmlText, Bucket=bucketName, Key=objectName, ACL='public-read')
        logger.info("response from bucket %s", response)

        return True, 'https://{}.s3.{}.amazonaws.com/{}'.format(bucketName, "us-east-2", objectName)

    except ClientError as e:
        logging.error(e)
        return False, 'error Uploading file'
