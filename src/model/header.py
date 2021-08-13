class Header(object):
    def __init__(self, user=None, echo_token=None, timestamp=None):
        self.user = user
        self.echoToken = echo_token
        self.timestamp = timestamp

    def __str__(self):
        return "user : {}, echoToken : {}, timestamp : {}".format(self.user, self.echoToken, self.timestamp)
