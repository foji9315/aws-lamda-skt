import test.test_utils.constants as constants

from src.model.header import Header
from src.model.request import Request
from src.model.reservation import Reservation, Hotel, ConfirmationNumber


def get_dummy_reservation_request():
    header = get_dummy_header()
    reservation = get_dummy_reservation()
    return Request(header, reservation)


def get_dummy_header():
    return Header(constants.USER, constants.ECHO_TOKEN, constants.TIME_STAMP)


def get_dummy_hotel():
    return Hotel(constants.UUID, constants.CODE, constants.OFFSET)


def get_dummy_confirmation_number_list(size):
    confirmation_list = []
    for i in range(size):
        confirmation = ConfirmationNumber(constants.CONFIRMATION_NUMBERS[i],
                                          constants.SOURCES[i],
                                          constants.GUESTS[i])
        confirmation_list.append(confirmation)
    return confirmation_list


def get_dummy_reservation():
    hotel = get_dummy_hotel()
    confirmation_numbers = get_dummy_confirmation_number_list(2)

    return Reservation(hotel,
                       constants.RESERVATION_ID,
                       confirmation_numbers,
                       constants.LAST_UPDATE_TIME_STAMP,
                       constants.LAST_UPDATE_OPERATOR_ID
                       )
