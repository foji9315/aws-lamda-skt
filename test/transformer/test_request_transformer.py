import json

from src.model.reservation import Reservation
from src.transformer.request_transformer import transform_event


def test_transform_event(json_input):
    event = json.loads(json_input)
    object_transformed = transform_event(event)
    assert True, isinstance(object_transformed, Reservation)
