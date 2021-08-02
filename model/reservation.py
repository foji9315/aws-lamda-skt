class Reservation(object):
    def __init__(self,
                 hotel=None,
                 reservationId=None,
                 confirmationNumbers=None,
                 lastUpdateTimestamp=None,
                 lastUpdateOperatorId=None):
        if confirmationNumbers is None:
            confirmationNumbers = []

        self.hotel = hotel
        self.reservationId = reservationId
        self.confirmationNumbers = confirmationNumbers
        self.lastUpdateTimestamp = lastUpdateTimestamp
        self.lastUpdateOperatorId = lastUpdateOperatorId

    def appendConfirmationNumber(self, confirmationNumber):
        self.confirmationNumbers.append(confirmationNumber)

    def __str__(self):
        return """Reservation(
            hotel : {}, 
            reservationId : {}, 
            confirmationNumbers : {}, 
            lastUpdateTimestamp : {}, 
            lastUpdateOperatorId : {})""".format(
            self.hotel,
            self.reservationId,
            self.confirmationNumbers,
            self.lastUpdateTimestamp,
            self.lastUpdateOperatorId
        )


class ConfirmationNumber(object):
    def __init__(self, confirmationNumber, source, guest):
        self.confirmationNumber = confirmationNumber
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
