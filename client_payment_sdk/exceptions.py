class ClientPaymentSDKError(Exception):
    def __init__(self, message, errors=None):
        super(ClientPaymentSDKError, self).__init__(message)
        self.errors = errors or {}


class RequestError(ClientPaymentSDKError):
    pass

class InternalServerError(ClientPaymentSDKError):
    pass


class MissArgumentError(ClientPaymentSDKError, ValueError):
    pass