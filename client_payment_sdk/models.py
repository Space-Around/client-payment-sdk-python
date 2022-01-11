# -*- coding: utf-8 -*-
from abc import ABC


class Model(ABC):
    @classmethod
    def from_dict(cls, model_dict):
        raise NotImplementedError

    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class InitPaymentResponse(Model, ABC):
    def __init__(self, status, payment_redirect_url, url, form_data):
        self.status = status
        self.payment_redirect_url = payment_redirect_url
        self.url = url
        self.form_data = form_data

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass


class NotificationPaymentResponse(Model, ABC):
    pass


class StatusPaymentResponse(Model, ABC):
    def __init__(self, status, payment_status, refund_status, last_payment_error_code=None, last_payment_error=None):
        self.status = status
        self.payment_status = payment_status
        self.refund_status = refund_status
        self.last_payment_error_code = last_payment_error_code
        self.last_payment_error = last_payment_error

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass


class BalanceResponse(Model, ABC):
    def __init__(self, status, balance):
        self.status = status
        self.balance = balance

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass


class WithdrawalResponse(Model, ABC):
    def __init__(self, status, withdrawal_request):
        self.status = status
        self.withdrawal_request = withdrawal_request

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass


class StatusWithdrawalResponse(Model, ABC):
    def __init__(self, status, withdrawal_request):
        self.status = status
        self.withdrawal_request = withdrawal_request

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass


class NotificationWithdrawalResponse(Model, ABC):
    pass


class WebhookDebugResponse(Model, ABC):
    def __init__(self, status, url, method, signature, params):
        self.status = status
        self.url = url
        self.method = method
        self.signature = signature
        self.params = params

    @classmethod
    def from_dict(cls, init_payment_dict):
        pass

    def to_dict(self):
        pass
