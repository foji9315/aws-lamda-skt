from src.model.header import Header
from src.model.reservation import Reservation, Hotel, ConfirmationNumber
from src.model.request import Request
from src.config.loggerconf import logger


def transform_event(body):
    xml_header = transform_header(body["header"])
    logger.info("header built {}".format(xml_header))

    xml_reservation = transform_reservation(body["reservation"])
    logger.info("Reservation built {}".format(xml_reservation))

    return Request(xml_header, xml_reservation)


def transform_header(header_request):
    return Header(header_request['echoToken'], header_request['timestamp'])


def transform_reservation(reservation_request):
    hotel = transform_hotel(reservation_request['hotel'])
    logger.debug("Hotel created {}".format(hotel))

    confirmation_numbers = transform_confirmation_numbers(reservation_request['confirmationNumbers'])
    logger.debug("This is the list of ConfirmationNumbers {}".format(confirmation_numbers))

    reservation_id = reservation_request['reservationId']
    last_update_timestamp = reservation_request['lastUpdateTimestamp']
    last_update_operator_id = reservation_request['lastUpdateOperatorId']

    return Reservation(hotel,
                       reservation_id,
                       confirmation_numbers,
                       last_update_timestamp,
                       last_update_operator_id)


def transform_hotel(hotel_request):
    return Hotel(hotel_request['uuid'], hotel_request['code'], hotel_request['offset'])


def transform_confirmation_numbers(request_confirmation_numbers):
    list_of_confirmation = []
    logger.debug("This is the number of confirmationNumber to convert : {}".format(len(request_confirmation_numbers)))
    for item in request_confirmation_numbers:
        list_of_confirmation.append(
            ConfirmationNumber(item['confirmationNumber'], item['source'], item['guest'])
        )
    return list_of_confirmation
