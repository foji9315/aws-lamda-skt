import json
import logging

from transformer.requestTransformer import transformEvent

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(context)
    logger.info("Event coming from API gateway : %s", event)

    transformEvent(event)

    return {
        'statusCode': 200,
        'body': json.dumps("Testing")
    }
