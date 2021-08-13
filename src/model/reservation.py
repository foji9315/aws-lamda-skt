class Reservation(object):
    def __init__(self,
                 hotel=None,
                 reservation_id=None,
                 confirmation_numbers=None,
                 last_update_timestamp=None,
                 last_update_operator_id=None):

        self.hotel = hotel
        self.reservationId = reservation_id
        self.confirmationNumbers = confirmation_numbers
        self.lastUpdateTimestamp = last_update_timestamp
        self.lastUpdateOperatorId = last_update_operator_id

    def __str__(self):
        confirmation_numbers = ",".join(map(str, self.confirmationNumbers))
        return """Reservation(
            hotel : {}, 
            reservationId : {}, 
            confirmationNumbers : [{}], 
            lastUpdateTimestamp : {}, 
            lastUpdateOperatorId : {})""".format(
            self.hotel,
            self.reservationId,
            confirmation_numbers,
            self.lastUpdateTimestamp,
            self.lastUpdateOperatorId
        )


class ConfirmationNumber(object):
    def __init__(self, confirmation_number, source, guest):
        self.confirmationNumber = confirmation_number
        self.source = source
        self.guest = guest

    def __str__(self):
        return "confirmationNumber : {}, source : {}, guest : {}".format(self.confirmationNumber,
                                                                         self.source,
                                                                         self.guest)


class Hotel(object):
    def __init__(self, uuid, code, offset):
        self.uuid = uuid
        self.code = code
        self.offset = offset

    def __str__(self):
        return "Hotel with uuid : {} , code : {} , offset : {} ".format(self.uuid, self.code, self.code)
