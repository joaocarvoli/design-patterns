from solid.after.order import Order
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass