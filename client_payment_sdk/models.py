# -*- coding: utf-8 -*-

class Model:
    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class InitPaymentResponse(Model):
    def __init__(self):
        self._status = None
        self._payment_redirect_url = None
        self._url = None
        self._form_data = None


class NotificationPaymentResponse(Model):
    pass


class StatusPaymentResponse(Model):
    def __init__(self):
        self._status = None
        self._payment_status = None
        self._refund_status = None
        self._last_payment_error_code = None
        self._last_payment_error = None


class BalanceResponse(Model):
    def __init__(self):
        self._status = None
        self._balance = None


class WithdrawalResponse(Model):
    def __init__(self):
        self._status = None
        self._withdrawal_request = None


class StatusWithdrawalResponse(Model):
    def __init__(self):
        self._status = None
        self._withdrawal_request = None


class NotificationWithdrawalResponse(Model):
    pass


class WebhookDebugResponse(Model):
    def __init__(self):
        self._status = None
        self._url = None
        self._method = None
        self._signature = None
        self._params = None
