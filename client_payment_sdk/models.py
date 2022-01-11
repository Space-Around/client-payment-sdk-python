# -*- coding: utf-8 -*-

class Model:
    @classmethod
    def from_dict(cls, model_dict):
        raise NotImplementedError

    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class InitPaymentResponse(Model):
    def __init__(self):
        self.status = None
        self.payment_redirect_url = None
        self.url = None
        self.form_data = None


class NotificationPaymentResponse(Model):
    pass


class StatusPaymentResponse(Model):
    def __init__(self):
        self.status = None
        self.payment_status = None
        self.refund_status = None
        self.last_payment_error_code = None
        self.last_payment_error = None


class BalanceResponse(Model):
    def __init__(self):
        self.status = None
        self.balance = None


class WithdrawalResponse(Model):
    def __init__(self):
        self.status = None
        self.withdrawal_request = None


class StatusWithdrawalResponse(Model):
    def __init__(self):
        self.status = None
        self.withdrawal_request = None


class NotificationWithdrawalResponse(Model):
    pass


class WebhookDebugResponse(Model):
    def __init__(self):
        self.status = None
        self.url = None
        self.method = None
        self.signature = None
        self.params = None
