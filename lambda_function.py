import json
import logging

from botocore.exceptions import ClientError

from converter.xml_converter import convert_request_to_xml
from repository.xml_repository import upload_xml
from transformer.request_transformer import transform_event

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(context)
    logger.info("Event coming from API gateway : %s", event)

    try:
        body = None
        if ('body' in event) and isinstance(event['body'], str):
            body = json.loads(event['body'])
        else:
            body = event

        reservation_request = transform_event(body)
        logger.info('Trying to convert object to XML file')

        xml_text = convert_request_to_xml(reservation_request)
        logger.info('Result of conversion %s', xml_text)

        text = upload_xml(xml_text,
                          "skt-task",
                          'reservation-{}.xml'.format(reservation_request.reservation.reservationId)
                          )
        return {
            'statusCode': 200,
            'body': json.dumps(text)
        }
    except Exception as e:
        logging.error(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error trying to upload xml file to S3 bucket')
        }
