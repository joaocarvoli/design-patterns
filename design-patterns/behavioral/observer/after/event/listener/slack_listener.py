from behavioral.observer.after.lib.slack import post_slack_message
from behavioral.observer.after.event.core import subscribe

def handler_user_registered_event(user):
    post_slack_message("sales", f"New user registered: {user.email}")

def setup_slack_event_handler():
    subscribe("user_registered", handler_user_registered_event)