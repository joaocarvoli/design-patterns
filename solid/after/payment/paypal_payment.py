from solid.after.auth.email_auth import EmailAuth
from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment

class PaypalPayment(Payment):
    def __init__(self, email: str, authorizer: EmailAuth):
        self.__email = email
        self.__authorizer = authorizer

    def pay(self, order: Order):
        if not self.__authorizer.is_authorized():
            print('You was not authorized')
            #  raise Exception('Not authorized')
        else:
            print("Processing paypal payment type")
            order.change_order_status(StatusType.PAID)