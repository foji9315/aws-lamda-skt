import json
import logging

from converter.xml_converter import convert_request_to_xml
from repository.xml_repository import upload_xml
from transformer.request_transformer import transform_event

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(context)
    logger.info("Event coming from API gateway : %s", event)

    body = None
    if ('body' in event) and isinstance(event['body'], str):
        body = json.loads(event['body'])
    else:
        body = event

    reservation_request = transform_event(body)
    logger.info('Trying to convert object to XML file')

    xml_text = convert_request_to_xml(reservation_request)
    logger.info('Result of conversion %s', xml_text)

    is_completed, text = upload_xml(xml_text,
                                    "skt-task",
                                    'reservation-{}.xml'.format(reservation_request.reservation.reservationId)
                                    )
    if is_completed:
        logger.info('Uploading success')
        return {
            'statusCode': 200,
            'body': json.dumps(text)
        }

    else:
        logger.info('Error Uploading')
        return {
            'statusCode': 500,
            'body': json.dumps(text)
        }
