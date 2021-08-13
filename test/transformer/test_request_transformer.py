import json

from src.model.reservation import Reservation
from src.transformer.request_transformer import transform_event

INPUT = '{"header": {"echoToken": "907f44fc-6b51-4237-8018-8a840fd87f04", "user": "kjasmd", "timestamp": "2018-03-07 20:59:575Z"}, "reservation": {"hotel": {"uuid": "3_c5f3c903-c43d-4967-88d1-79ae81d00fcb", "code": "TASK1", "offset": "+06:00"}, "reservationId": 12345, "confirmationNumbers": [{"confirmationNumber": "12345", "source": "ENCORA", "guest": "Arturo Miguel Vargas"}, {"confirmationNumber": "67890", "source": "NEARSOFT", "guest": "Carlos Hernández"}], "lastUpdateTimestamp": "2018-03-07 20:59:541Z", "lastUpdateOperatorId": "task.user"}}'


def set_up():
    return json.loads(INPUT)


def test_transform_event():
    json_input = set_up()
    object_transformed = transform_event(json_input)
    assert True, isinstance(object_transformed, Reservation)
