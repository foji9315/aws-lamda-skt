import xml.etree.ElementTree as ET
from xml.dom import minidom
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def convert_request_to_xml(reservation_request):
    # root element
    root = ET.Element('Reservation')

    # header sub-element
    xml_header = ET.SubElement(root, 'header')

    build_xml_header(reservation_request.header, xml_header)

    # body sub-element
    body = ET.SubElement(root, 'body')
    build_xml_body(reservation_request.reservation, body)

    return minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")


def build_xml_header(header, xml_header):
    xml_echo_token = ET.SubElement(xml_header, 'echoToken')
    xml_echo_token.text = header.echoToken

    xml_timestamp = ET.SubElement(xml_header, 'timestamp')
    xml_timestamp.text = header.timestamp


def build_xml_body(reservation, xml_body):
    hotel = ET.SubElement(xml_body, 'hotel')
    build_xml_hotel(reservation.hotel, hotel)

    reservation_id = ET.SubElement(xml_body, 'reservationId')
    reservation_id.text = str(reservation.reservationId)

    reservations = ET.SubElement(xml_body, 'reservations')
    build_xml_reservations(reservation.confirmationNumbers, reservations)

    last_update_timestamp = ET.SubElement(xml_body, 'lastUpdateTimestamp')
    last_update_timestamp.text = reservation.lastUpdateTimestamp

    last_update_operator_id = ET.SubElement(xml_body, 'lastUpdateOperatorId')
    last_update_operator_id.text = reservation.lastUpdateOperatorId


def build_xml_hotel(hotel, xml_hotel):
    uuid = ET.SubElement(xml_hotel, 'uuid')
    uuid.text = hotel.uuid

    code = ET.SubElement(xml_hotel, 'code')
    code.text = hotel.code

    offset = ET.SubElement(xml_hotel, 'offset')
    offset.text = hotel.offset


def build_xml_reservations(confirmation_numbers, xml_reservations):
    for confirmation in confirmation_numbers:
        xml_reservation = ET.SubElement(xml_reservations, 'reservation', {'source': confirmation.source})

        xml_info = ET.SubElement(xml_reservation, 'info', {'confirmationNumber': str(confirmation.confirmationNumber)})
        build_xml_info(confirmation.guest, xml_info)


def build_xml_info(guest, xml_info):
    names = guest.split(" ")

    first_name = ET.SubElement(xml_info, 'firstName')
    first_name.text = names[0]

    last_name = ET.SubElement(xml_info, 'lastName')
    last_name.text = names[1]
