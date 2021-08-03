import json
import logging

from converter.xmlConverter import convertRequestToXML
from repository.xmlRepository import uploadXML
from transformer.requestTransformer import transformEvent

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(context)
    logger.info("Event coming from API gateway : %s", event)

    reservationRequest = transformEvent(event)
    logger.info('Trying to convert object to XML file')

    xmlText = convertRequestToXML(reservationRequest)
    logger.info('Result of conversion %s', xmlText)

    isCompleted, text = uploadXML(xmlText,
                                  "skt-task",
                                  'reservation-{}.xml'.format(reservationRequest.reservation.reservationId)
                                  )
    if isCompleted:
        logger.info('Uploading success')
        return {
            'statusCode': 200,
            'URL': json.dumps(text)
        }

    else:
        logger.info('Error Uploading')
        return {
            'statusCode': 500,
            'message': json.dumps(text)
        }
