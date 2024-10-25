from order import Order
from solid.after.status_type import StatusType


class Payment:
    def __init__(self, order: Order):
        self.__order = order

    def pay_with_debit(self, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        self.__order.change_order_status(StatusType.PAID)

    def pay_with_credit(self, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        self.__order.change_order_status(StatusType.PAID)