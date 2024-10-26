from solid.after.auth.auth_method import AuthMethod
from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment

class PaypalPayment(Payment):
    def __init__(self, email: str, authorizer: AuthMethod):
        self.__email = email
        self.__authorizer = authorizer

    def pay(self, order: Order):
        self.__authorizer.authorize()

        if not self.__authorizer.is_authorized():
            print('You was not authorized')
        else:
            print("Processing paypal payment type")
            order.change_order_status(StatusType.PAID)