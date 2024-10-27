from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan
from behavioral.observer.after.event.listener.email_listener import setup_email_event_handler
from behavioral.observer.after.event.listener.log_listener import setup_log_event_handler
from behavioral.observer.after.event.listener.slack_listener import setup_slack_event_handler

def main():
    # Setting up the event handlers observers
    setup_log_event_handler()
    setup_slack_event_handler()
    setup_email_event_handler()

    # register a new user
    register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

    # send a password reset message
    password_forgotten("hi@arjanegges.com")

    # upgrade the plan
    upgrade_plan("hi@arjanegges.com")

if __name__ == "__main__":
    main()