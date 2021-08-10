import os
import re
import logging


def striplines(m):
    m = re.compile(r'[\t]').sub(' ', str(m))
    return re.compile(r'[\r\n]').sub('', str(m))


def exception(e):
    logger.exception(striplines(e))


def info(msg):
    logger.info(msg)


def error(msg):
    logger.error(msg)


def debug(msg):
    logger.debug(msg)


logger = logging.getLogger()
if "LOGGING_LEVEL" in os.environ:
    if os.environ["LOGGING_LEVEL"] == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif os.environ["LOGGING_LEVEL"] == "CRITICAL":
        logger.setLevel(logging.CRITICAL)
    elif os.environ["LOGGING_LEVEL"] == "WARNING":
        logger.setLevel(logging.WARNING)
    elif os.environ["LOGGING_LEVEL"] == "INFO":
        logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.INFO)

