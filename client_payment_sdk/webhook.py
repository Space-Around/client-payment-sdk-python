from .sign import sign
from .models import WebhookData
from .exceptions import SignatureVerificationError, PassedTypeError


class Webhook:
    @staticmethod
    def verify_signature(endpoint, method, data, secret):
        if not isinstance(data, WebhookData):
            raise PassedTypeError('data must be WebhookData')

        payload = {}

        for key in data:
            if key != 'signature':
                payload[key] = data[key]

        if sign(endpoint, method, payload, secret) != data.signature:
            raise SignatureVerificationError('signatures not match')

        return True

