
class FSApiException(Exception):
    pass


class ConnectionError(FSApiException):
    pass


class OutOfRangeException(FSApiException):
    pass


class InvalidSessionException(FSApiException):
    pass
