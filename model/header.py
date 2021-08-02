class Header(object):
    def __init__(self, echoToken=None, timestamp=None):
        self.echoToken = echoToken
        self.timestamp = timestamp

    def __str__(self):
        return "echoToken : {}, timestamp : {}".format(self.echoToken, self.timestamp)