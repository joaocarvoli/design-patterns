from status_type import StatusType

class Order:
    def __init__(self):
        self.__items = []
        self.__quantities = []
        self.__prices = []
        self.__status = StatusType.OPEN

    def add_item(self, name, quantity, price):
        self.__items.append(name)
        self.__quantities.append(quantity)
        self.__prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.__prices)):
            total += self.__quantities[i] * self.__prices[i]
        return total

    def change_order_status(self, status: StatusType):
        self.__status = status