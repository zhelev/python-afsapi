class FSApiException(Exception):
    pass


class NotImplementedException(Exception):
    pass


class ConnectionError(FSApiException):
    pass


class OutOfRangeException(FSApiException):
    pass


class InvalidPinException(FSApiException):
    pass


class InvalidSessionException(FSApiException):
    pass
