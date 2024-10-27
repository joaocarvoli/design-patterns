from behavioral.observer.after.lib.log import log
from behavioral.observer.after.event.core import subscribe

def handler_user_registered_event(user):
    log(f"New user registered with email address: {user.email}")

def handler_user_password_forgotten_event(user):
    log(f"User {user.email} has forgotten their password and is requesting a reset")

def handle_user_upgraded_plan_event(user):
    log(f"User {user.email} has upgraded their plan")

def setup_log_event_handler():
    subscribe("user_registered", handler_user_registered_event)
    subscribe("user_password_forgotten", handler_user_password_forgotten_event)
    subscribe("user_upgraded_plan", handle_user_upgraded_plan_event)