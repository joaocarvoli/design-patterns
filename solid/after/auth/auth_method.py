from abc import ABC, abstractmethod


class AuthMethod(ABC):
    __authorized = False

    def is_authorized(self) -> bool:
        return self.__authorized

    def set_authorization(self, authorized: bool):
        self.__authorized = authorized

    @abstractmethod
    def authorize(self):
        """Implement specific authorization logic in subclasses"""
        pass
