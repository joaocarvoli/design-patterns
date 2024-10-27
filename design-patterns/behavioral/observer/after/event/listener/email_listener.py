from behavioral.observer.after.event.core import subscribe
from behavioral.observer.after.lib.email import send_email


def handler_user_registered_event(user):
    send_email(
        user.name,
        user.email,
        "Welcome to our platform",
        f"Hi {user.name},\n\nWelcome to our platform! We are excited to have you on board.\n\nBest,\nYour Team"
    )

def handler_user_password_forgotten_event(user):
    send_email(
        user.name,
        user.email,
        "Password reset",
        f"Hi {user.name},\n\nWe have received a request to reset your password. Please use the following code to reset your password: {user.reset_code}\n\nBest,\nYour Team"
    )

def handler_user_upgraded_plan_event(user):
    send_email(
        user.name,
        user.email,
        "Plan upgrade",
        f"Hi {user.name},\n\nCongratulations! You have successfully upgraded your plan.\n\nBest,\nYour Team"
    )

def setup_email_event_handler():
    subscribe("user_registered", handler_user_registered_event)
    subscribe("user_password_forgotten", handler_user_password_forgotten_event)
    subscribe("user_upgraded_plan", handler_user_upgraded_plan_event)