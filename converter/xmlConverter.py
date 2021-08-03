import xml.etree.ElementTree as ET
from xml.dom import minidom
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def convertRequestToXML(reservationRequest):
    # root element
    root = ET.Element('Reservation')

    # header sub-element
    xmlHeader = ET.SubElement(root, 'header')

    buildXmlHeader(reservationRequest.header, xmlHeader)

    # body sub-element
    body = ET.SubElement(root, 'body')
    buildXmlBody(reservationRequest.reservation, body)

    return minidom.parseString(ET.tostring(root)).toprettyxml(indent = "    ")


def buildXmlHeader(header, xmlHeader):
    xmlEchoToken = ET.SubElement(xmlHeader, 'echoToken')
    xmlEchoToken.text = header.echoToken

    xmlTimestamp = ET.SubElement(xmlHeader, 'timestamp')
    xmlTimestamp.text = header.timestamp


def buildXmlBody(reservation, xmlBody):
    hotel = ET.SubElement(xmlBody, 'hotel')
    buildXmlHotel(reservation.hotel, hotel)

    reservationId = ET.SubElement(xmlBody, 'reservationId')
    reservationId.text = str(reservation.reservationId)

    reservations = ET.SubElement(xmlBody, 'reservations')
    buildXmlReservations(reservation.confirmationNumbers, reservations)

    lastUpdateTimestamp = ET.SubElement(xmlBody, 'lastUpdateTimestamp')
    lastUpdateTimestamp.text = reservation.lastUpdateTimestamp

    lastUpdateOperatorId = ET.SubElement(xmlBody, 'lastUpdateOperatorId')
    lastUpdateOperatorId.text = reservation.lastUpdateOperatorId


def buildXmlHotel(hotel, xmlHotel):
    uuid = ET.SubElement(xmlHotel, 'uuid')
    uuid.text = hotel.uuid

    code = ET.SubElement(xmlHotel, 'code')
    code.text = hotel.code

    offset = ET.SubElement(xmlHotel, 'offset')
    offset.text = hotel.offset


def buildXmlReservations(confirmationNumbers, xmlReservations):
    for confirmation in confirmationNumbers:
        xmlReservation = ET.SubElement(xmlReservations, 'reservation', {'source': confirmation.source})

        xmlInfo = ET.SubElement(xmlReservation, 'info', {'confirmationNumber': str(confirmation.confirmationNumber)})
        buildXmlInfo(confirmation.guest, xmlInfo)


def buildXmlInfo(guest, xmlInfo):
    names = guest.split(" ")

    firstName = ET.SubElement(xmlInfo, 'firstName')
    firstName.text = names[0]

    lastName = ET.SubElement(xmlInfo, 'lastName')
    lastName.text = names[1]
