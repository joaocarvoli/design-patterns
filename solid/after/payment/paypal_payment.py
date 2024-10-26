from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment

class PaypalPayment(Payment):
    def __init__(self, email: str):
        self.__email = email

    def pay(self, order: Order):
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.__email}")
        order.change_order_status(StatusType.PAID)