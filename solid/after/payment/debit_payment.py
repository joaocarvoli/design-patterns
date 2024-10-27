from solid.after.auth.auth_method import AuthMethod
from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment

class DebitPayment(Payment):
    def __init__(self, security_code: str, authorizer: AuthMethod):
        self.__security_code = security_code
        self.__authorizer = authorizer

    def pay(self, order: Order):
        self.__authorizer.authorize()

        if not self.__authorizer.is_authorized():
            print('You was not authorized')
        else:
            print("Processing debit payment type")
            order.change_order_status(StatusType.PAID)