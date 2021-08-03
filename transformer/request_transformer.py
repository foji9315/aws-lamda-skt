import logging

from model.header import Header
from model.request import Request
from model.reservation import ConfirmationNumber
from model.reservation import Hotel
from model.reservation import Reservation

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def transform_event(body):
    header = transform_header(body["header"])
    logger.info("header built %s", header)

    reservation = transform_reservation(body["reservation"])
    logger.info("Reservation built %s", reservation)

    return Request(header, reservation)


def transform_header(header_request):
    return Header(header_request['echoToken'], header_request['timestamp'])


def transform_reservation(reservation_request):
    hotel = transform_hotel(reservation_request['hotel'])
    logger.info("Hotel created %s", hotel)

    confirmation_numbers = transform_confirmation_numbers(reservation_request['confirmationNumbers'])
    logger.info("This is the list of ConfirmationNumbers %s", confirmation_numbers)

    reservation_id = reservation_request['reservationId']
    last_update_timestamp = reservation_request['lastUpdateTimestamp']
    last_update_operator_id = reservation_request['lastUpdateOperatorId']

    return Reservation(hotel, reservation_id, confirmation_numbers, last_update_timestamp, last_update_operator_id)


def transform_hotel(hotel_request):
    return Hotel(hotel_request['uuid'], hotel_request['code'], hotel_request['offset'])


def transform_confirmation_numbers(request_confirmation_numbers):
    list_of_confirmation = []
    logger.info("This is the number of confirmationNumber to convert : %s", len(request_confirmation_numbers))
    for item in request_confirmation_numbers:
        list_of_confirmation.append(
            ConfirmationNumber(item['confirmationNumber'], item['source'], item['guest'])
        )
    return list_of_confirmation
