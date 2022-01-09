# -*- coding: utf-8 -*-
from copy import deepcopy
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

    def _request(self, url, method, data=None, request_id=None):
        headers = None
        if request_id is not None:
            headers = {'X-Request-ID': request_id}

        if method == 'get':
            response = requests.get(url, params=data, headers=headers)
        else:
            response = requests.post(url, params=data, headers=headers)

        if response.headers['Content-Type'].find('application/json') != -1:
            return response.json(parse_float=decimal.Decimal)
        else:
            return response.content

    def _get(self, url, data):
        return self._request(url, 'get', data)

    def _post(self, url, data):
        return self._request(url, 'post', data)

    def init(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        endpoint = '/init'

        response = self._send_request(endpoint, params)

        return response

    def payment_status(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        pass

    def balance(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        pass

    def refund(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        pass

    def refund_status(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        pass
