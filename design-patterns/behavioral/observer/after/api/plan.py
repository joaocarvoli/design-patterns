from behavioral.observer.after.event.core import post_event
from behavioral.observer.after.lib.db import find_user


def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    post_event("user_upgraded_plan", user)