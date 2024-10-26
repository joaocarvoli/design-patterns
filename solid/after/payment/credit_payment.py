from solid.after.auth.sms_auth import SMSAuth
from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment


class CreditPayment(Payment):
    def __init__(self, security_code: str, authorizer: SMSAuth):
        self.__security_code = security_code
        self.__authorizer = authorizer

    def pay(self, order: Order):
        if not self.__authorizer.is_authorized():
            print('You was not authorized')
            #  raise Exception('Not authorized')
        else:
            print("Processing credit payment type")
            order.change_order_status(StatusType.PAID)