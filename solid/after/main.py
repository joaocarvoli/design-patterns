from order import Order
from payment.credit_payment import CreditPayment
from payment.paypal_payment import PaypalPayment


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    payment_credit = CreditPayment("0372846")
    payment_paypal = PaypalPayment("joaovictor@gmail.com")

    print(f'Order total price is {order.total_price()}')

    payment_credit.pay(order)
    payment_paypal.pay(order)

