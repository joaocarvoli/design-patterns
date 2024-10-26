from solid.after.order import Order, StatusType
from solid.after.payment.payment import Payment


class CreditPayment(Payment):
    def __init__(self, security_code: str):
        self.__security_code = security_code

    def pay(self, order: Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.__security_code}")
        order.change_order_status(StatusType.PAID)