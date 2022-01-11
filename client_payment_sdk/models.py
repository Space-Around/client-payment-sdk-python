# -*- coding: utf-8 -*-

class Model:
    def __repr__(self):
        state = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(state))


class InitPaymentResponse(Model):
    pass


class NotificationPaymentResponse(Model):
    pass


class StatusResponse(Model):
    pass


class BalanceResponse(Model):
    pass


class StatusPaymentResponse(Model):
    pass


class WithdrawalResponse(Model):
    pass


class StatusWithdrawalResponse(Model):
    pass


class NotificationWithdrawalResponse(Model):
    pass