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
    def __init__(self, status=None, payment_redirect_url=None, url=None, form_data=None):
        super(InitPaymentResponse, self).__init__()
        self.status = status
        self.payment_redirect_url = payment_redirect_url
        self.url = url
        self.form_data = form_data

    @classmethod
    def from_dict(cls, init_payment_dict):
        keys = ('status', 'payment_redirect_url', 'url', 'form_data')

        for key in keys:
            if key not in init_payment_dict:
                init_payment_dict[key] = None

        return cls(init_payment_dict['status'], init_payment_dict['payment_redirect_url'], init_payment_dict['url'],
                   init_payment_dict['form_data'])

    def to_dict(self):
        pass


class NotificationPaymentResponse(Model, ABC):
    pass


class StatusPaymentResponse(Model, ABC):
    def __init__(self, status, payment_status, refund_status, last_payment_error_code=None, last_payment_error=None):
        super(StatusPaymentResponse, self).__init__()
        self.status = status
        self.payment_status = payment_status
        self.refund_status = refund_status
        self.last_payment_error_code = last_payment_error_code
        self.last_payment_error = last_payment_error

    @classmethod
    def from_dict(cls, status_payment_dict):
        return cls(status_payment_dict['status'], status_payment_dict['payment_status'],
                   status_payment_dict['refund_status'], status_payment_dict['last_payment_error_code'],
                   status_payment_dict['last_payment_error'])

    def to_dict(self):
        pass


class BalanceResponse(Model, ABC):
    def __init__(self, status, balance):
        super(BalanceResponse, self).__init__()
        self.status = status
        self.balance = balance

    @classmethod
    def from_dict(cls, balance_dict):
        return cls(balance_dict['status'], balance_dict['balance'])

    def to_dict(self):
        pass


class WithdrawalResponse(Model, ABC):
    def __init__(self, status, withdrawal_request):
        super(WithdrawalResponse, self).__init__()
        self.status = status
        self.withdrawal_request = withdrawal_request

    @classmethod
    def from_dict(cls, withdrawal_dict):
        return cls(withdrawal_dict['status'], withdrawal_dict['withdrawal_request'])

    def to_dict(self):
        pass


class StatusWithdrawalResponse(Model, ABC):
    def __init__(self, status, withdrawal_request):
        super(StatusWithdrawalResponse, self).__init__()
        self.status = status
        self.withdrawal_request = withdrawal_request

    @classmethod
    def from_dict(cls, status_withdrawal_dict):
        return cls(status_withdrawal_dict['status'], status_withdrawal_dict['withdrawal_request'])

    def to_dict(self):
        pass


class NotificationWithdrawalResponse(Model, ABC):
    pass


class WebhookDebugResponse(Model, ABC):
    def __init__(self, status, url, method, signature, params):
        super(WebhookDebugResponse, self).__init__()
        self.status = status
        self.url = url
        self.method = method
        self.signature = signature
        self.params = params

    @classmethod
    def from_dict(cls, webhook_debug_dict):
        return cls(webhook_debug_dict['status'], webhook_debug_dict['url'], webhook_debug_dict['method'],
                   webhook_debug_dict['signature'], webhook_debug_dict['params'])

    def to_dict(self):
        pass