from solid.after.auth.auth_method import AuthMethod
import secrets

from solid.after.random_picker import choose_a_random_item


class SMSAuth(AuthMethod):
    __validation_mocked_output = [False, True]

    def verify_code(self, code: str):
        print(f'Verifying code {code}')

        result = choose_a_random_item(self.__validation_mocked_output) # Representing some logic
        self.set_authorization(result)
