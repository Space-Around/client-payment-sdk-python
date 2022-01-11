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


class NotificationPaymentResponse(Model, ABC):
    pass


class StatusPaymentResponse(Model, ABC):
    def __init__(self):
        self.status = None
        self.payment_status = None
        self.refund_status = None
        self.last_payment_error_code = None
        self.last_payment_error = None


class BalanceResponse(Model, ABC):
    def __init__(self):
        self.status = None
        self.balance = None


class WithdrawalResponse(Model, ABC):
    def __init__(self):
        self.status = None
        self.withdrawal_request = None


class StatusWithdrawalResponse(Model, ABC):
    def __init__(self):
        self.status = None
        self.withdrawal_request = None


class NotificationWithdrawalResponse(Model, ABC):
    pass


class WebhookDebugResponse(Model, ABC):
    def __init__(self):
        self.status = None
        self.url = None
        self.method = None
        self.signature = None
        self.params = None
