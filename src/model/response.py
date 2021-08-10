import json


class Response(object):

    def __init__(self, status_code, body_text):
        self.statusCode = status_code
        self.body = body_text

    def get_response(self):
        return {
            "statusCode": self.statusCode,
            "body": json.dumps(self.body)
        }
