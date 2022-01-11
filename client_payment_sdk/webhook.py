from .sign import sign
from .models import NotificationPaymentResponse, NotificationWithdrawalResponse
from .exceptions import SignatureVerificationError
from copy import deepcopy


class Webhook:
    def __init__(self, data, api_secret):
        self._data = data
        self._api_secret = api_secret

    def verify_signature(self):
        endpoint = ''
        method = 'POST'
        payload = deepcopy(self._data)
        del payload

        if sign(endpoint, method, payload, self._api_secret) != self._data['signature']:
            raise SignatureVerificationError(' signatures not match')

        return True
