# -*- coding: utf-8 -*-
import decimal

import requests


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

        response = requests.post(self.URL + endpoint, json=params, headers=headers)

        return response.json(parse_float=decimal.Decimal)

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

