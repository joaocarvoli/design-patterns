import secrets

from solid.after.auth.auth_method import AuthMethod
from solid.after.random_picker import choose_a_random_item


class EmailAuth(AuthMethod):
    __validation_mocked_output = [False, True]

    def verify_email(self, email: str):
        print(f'Verifying email {email}')

        result = choose_a_random_item(self.__validation_mocked_output) # Representing some logic
        self.set_authorization(result)