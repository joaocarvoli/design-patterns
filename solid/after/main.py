from order import Order
from payment import Payment

if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    payment = Payment(order)

    print(order.total_price())
    payment.pay_with_debit( "0372846")