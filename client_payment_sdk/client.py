# -*- coding: utf-8 -*-
import decimal

import requests
from .exceptions import PaymentError


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

        try:
            if method == 'get':
                response = requests.get(url, params=data, headers=headers)
            else:
                response = requests.post(url, data, headers=headers)

            if response.status_code != 200:
                raise PaymentError(f'Server not available: {response.status_code}')

            if response.headers['Content-Type'].find('application/json') != -1:
                return response.json(parse_float=decimal.Decimal)
            else:
                return response.content.decode('utf-8')
        except requests.ConnectionError as error:
            raise PaymentError(error)

    def _get(self, url, data=None):
        return self._request(url, 'get', data)

    def _post(self, url, data=None):
        return self._request(url, 'post', data)

    def init(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        endpoint = '/init'

        return self._post(self.URL + endpoint, params)

    def payment_status(self, params):
        """
        Payment Initiation

        # Arguments

        # Raises

        # Returns

        """
        endpoint = '/status'

        return self._get(self.URL + endpoint, params)

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
