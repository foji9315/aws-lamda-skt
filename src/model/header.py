class Header(object):
    def __init__(self, echo_token=None, timestamp=None):
        self.echoToken = echo_token
        self.timestamp = timestamp

    def __str__(self):
        return "echoToken : {}, timestamp : {}".format(self.echoToken, self.timestamp)
