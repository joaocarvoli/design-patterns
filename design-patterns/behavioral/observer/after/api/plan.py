from observer.after.lib.db import find_user
from observer.after.event.core import post_event



def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    post_event("user_upgraded_plan", user)