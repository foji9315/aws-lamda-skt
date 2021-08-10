import json
import os

from src.config.loggerconf import logger
from src.converter.xml_converter import convert_request_to_xml
from src.model.response import Response
from src.repository.xml_repository import upload_xml
from src.transformer.request_transformer import transform_event


def lambda_handler(event, context):
    logger.debug(os.environ)
    logger.debug(context)
    logger.info("Event coming from API gateway : %s", event)

    response = None

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

        bucket_name = os.environ['BUCKET_NAME']
        body = upload_xml(xml_text,
                          bucket_name,
                          'reservation-{}.xml'.format(reservation_request.reservation.reservationId)
                          )
        logger.info("Uploading success")
        response = Response(200, body)

    except Exception as e:
        logger.info("Error uploading {}".format(e))
        response = Response(500, 'Error Uploading')

    finally:
        return response.get_response()
