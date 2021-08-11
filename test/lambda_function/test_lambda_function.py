import json
import os

import pytest

from src.lambda_function import lambda_handler
from src.model.response import Response


def test_lambda_happy_path(s3_test, json_input):
    """
    unit testing for happy path considering that we are receiving a dict directly
    :param s3_test: mock bucket
    :param json_input: json read from .json file
    """
    event = json.loads(json_input)
    result = lambda_handler(event, None)
    assert True, isinstance(result, Response)


def test_lambda_happy_path_gateway(s3_test, json_input):
    """
    unit testing for happy path considering that we are receiving an event from gateway
    :param s3_test: mock bucket
    :param json_input: json read from .json file
    """
    gateway_event = {'body': json_input}
    os.environ["LOGGING_LEVEL"] = 'DEBUG'
    result = lambda_handler(gateway_event, None)
    assert True, isinstance(result, Response)


def test_lambda_raise_exception(json_input):
    """
    unit testing raisins any exception and logLevel ERROR
    :param json_input: json read from .json file
    """
    gateway_event = {'body': json_input}
    os.environ["LOGGING_LEVEL"] = 'ERROR'
    os.environ["BUCKET_NAME"] = 'name'
    with pytest.raises(Exception):
        result = lambda_handler(gateway_event, None)
        assert True, isinstance(result, Response)
        assert 500 == result.statusCode
