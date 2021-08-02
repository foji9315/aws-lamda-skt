import logging

from model.header import Header
from model.request import Request
from model.reservation import ConfirmationNumber
from model.reservation import Hotel
from model.reservation import Reservation

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def transformEvent(body):
    header = transformHeader(body["header"])
    logger.info("header built %s", header)

    reservation = transformReservation(body["reservation"])
    logger.info("Reservation buil %s", reservation)

    return Request(header, reservation)


def transformHeader(headerRequest):
    return Header(headerRequest['echoToken'], headerRequest['timestamp'])


def transformReservation(reservationRequest):
    hotel = transformHotel(reservationRequest['hotel'])
    logger.info("Hotel created %s", hotel)

    confirmationNumbers = transformConfrimationNumbers(reservationRequest['confirmationNumbers'])
    logger.info("This is the list of ConfirmationNumbers %s", confirmationNumbers)

    reservationId = reservationRequest['reservationId']
    lastUpdateTimestamp = reservationRequest['lastUpdateTimestamp']
    lastUpdateOperatorId = reservationRequest['lastUpdateOperatorId']

    return Reservation(hotel, reservationId, confirmationNumbers, lastUpdateTimestamp, lastUpdateOperatorId)


def transformHotel(hotelRequest):
    return Hotel(hotelRequest['uuid'], hotelRequest['code'], hotelRequest['offset'])


def transformConfrimationNumbers(requestConfirmationNumbers):
    listOfConfirmation = []
    logger.info("This is the number of confirmationNumber to convert : %s", len(requestConfirmationNumbers))
    for item in requestConfirmationNumbers:
        listOfConfirmation.append(
            ConfirmationNumber(item['confirmationNumber'], item['source'], item['guest'])
        )
    return listOfConfirmation
