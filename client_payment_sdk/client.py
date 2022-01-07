# -*- coding: utf-8 -*-
import decimal
import requests
from jwcrypto import jws, jwk
from jwcrypto.common import json_encode, json_decode


class ClientPaymentSDK(object):
    """
    ClientPaymentSDK Class
    """
    URL = 'https://sbank.gogo.vc'

    def __init__(self, public_id, api_secret):
        self._public_id = public_id
        self._api_secret = api_secret

    def _send_request(self, endpoint, params=None, request_id=None):
        headers = None
        if request_id is not None:
            headers = {'X-Request-ID': request_id}

        response = requests.get(self.URL + endpoint, params=params, headers=headers)

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            return response.json(parse_float=decimal.Decimal)
        else:
            return response.content

    def init(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        endpoint = '/init'
        header = {'alg': 'HS256'}

        key = jwk.JWK.from_password(self._api_secret)

        sorted_param = dict(sorted(params.items(), key=lambda x: x[0]))

        payload_dict = {'PATH': endpoint, 'GET': sorted_param}
        payload_str = str(payload_dict).replace('\'', '"').replace(' ', '')

        jwstoken = jws.JWS(payload_str.encode('utf-8'))
        jwstoken.add_signature(key, None, json_encode(header), json_encode({"kid": key.thumbprint()}))
        jws_data = json_decode(jwstoken.serialize())

        params['signature'] = jws_data['signature']

        response = self._send_request(endpoint, params)

        return response

    def init_3ds(self, device):
        pass

    def get_status(self, param):
        pass

    def get_balance(self, param):
        pass

    def withdrawal(self, param):
        pass
