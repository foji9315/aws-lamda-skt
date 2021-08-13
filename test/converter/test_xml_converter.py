from src.converter.xml_converter import convert_request_to_xml
from test.test_utils.object_factory import get_dummy_reservation_request


def test_xml_converter_success():
    request = get_dummy_reservation_request()
    xml_text = convert_request_to_xml(request)
    assert xml_text != ''
