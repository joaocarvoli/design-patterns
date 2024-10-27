from behavioral.observer.after.event.core import post_event
from behavioral.observer.after.lib.db import create_user, find_user
from behavioral.observer.after.lib.stringtools import get_random_string


def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)
    post_event("user_registered", user)

def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)
    post_event("password_forgotten", user)