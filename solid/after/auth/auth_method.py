from abc import ABC

class AuthMethod(ABC):
    __authorized = False

    def is_authorized(self) -> bool:
        return self.__authorized

    def set_authorization(self, authorized: bool):
        self.__authorized = authorized
