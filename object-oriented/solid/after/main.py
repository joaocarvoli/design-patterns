from solid.after.auth.captcha_method import CaptchaMethod
from solid.after.auth.email_auth import EmailAuth
from solid.after.auth.sms_auth import SMSAuth
from solid.after.order import Order
from solid.after.payment.credit_payment import CreditPayment
from solid.after.payment.debit_payment import DebitPayment
from solid.after.payment.paypal_payment import PaypalPayment

if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    email_authorizer = EmailAuth()
    sms_authorizer = SMSAuth()
    captcha_authorizer = CaptchaMethod()

    # Probably doesn't make sense some payments supports some authorizers but this is only to ilustrate the principles
    payment_credit = CreditPayment("0372846", sms_authorizer)
    payment_paypal = PaypalPayment("joaovictor@gmail.com", email_authorizer)
    payment_debit = DebitPayment("0372846", captcha_authorizer)

    print(f'Order total price is {order.total_price()}')

    payment_credit.pay(order)
    payment_paypal.pay(order)
    payment_debit.pay(order)

