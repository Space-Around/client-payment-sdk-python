# -*- coding: utf-8 -*-
import requests
from .exceptions import RequestError, InternalServerError


class ClientPaymentSDK:
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

            if response.status_code == 400:
                error = response.json()
                code = ['code']
                message = error['message']

                raise RequestError(f'error code: {code}, message: {message}')
            elif response.status_code == 500:
                error = response.json()
                code = error['code']
                message = error['message']

                raise InternalServerError(f'error code: {code}, message: {message}')
            elif response.status_code != 200:
                raise RequestError(f'Server not available: {response.status_code}')

            if response.headers['Content-Type'].find('application/json') != -1:
                return response.json()
            else:
                return response.content.decode('utf-8')
        except requests.ConnectionError as error:
            raise RequestError(error)

    def _get(self, url, data=None):
        return self._request(url, 'get', data)

    def _post(self, url, data=None):
        return self._request(url, 'post', data)

    def init(self, params):
        """
        Payment Initiation

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does fail
        InternalServerError: If internal server error

        # Returns
        str | dict
        """
        endpoint = '/init'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._post(self.URL + endpoint, params)

    def status(self, params):
        """
        Get Payment Status

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does failed
        InternalServerError: If internal server error

        # Returns
        str | dict
        """
        endpoint = '/status'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._get(self.URL + endpoint, params)

    def balance(self, params):
        """
        Get Merchant Balance

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does failed
        InternalServerError: If internal server error

        # Returns
        str | dict
        """
        endpoint = '/balance'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._get(self.URL + endpoint, params)

    def withdrawal(self, params):
        """
        Withdrawal Initiation

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does failed
        InternalServerError: If internal server error

        # Returns
        str | dict
        """
        endpoint = '/withdrawal_request'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._get(self.URL + endpoint, params)

    def withdrawal_status(self, params):
        """
        Get Withdrawal Status

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does failed
        InternalServerError: If internal server error

        # Returns
        str | dicts
        """
        endpoint = '/withdrawal_request'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._get(self.URL + endpoint, params)

    def webhook_sign_debug(self, params):
        """
        Debug Webhook Sign

        # Arguments
        params (dict)

        # Raises
        RequestError: If request does failed
        InternalServerError: If internal server error

        # Returns
        str | dicts
        """
        endpoint = '/webhook_sign_debug'

        if not isinstance(params, dict):
            raise ValueError('passed value must be dict')

        return self._get(self.URL + endpoint, params)
