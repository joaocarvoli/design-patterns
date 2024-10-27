from typing import Callable, Any

subscribers = dict()

def subscribe(event_type: str, subscriber: Callable[[Any], None]):
    """
    Method responsible for subscribing to an event
    :param event_type: The identifier of the event
    :param subscriber: The function to be called when the event is triggered
    :return:
    """

    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(subscriber)

def post_event(event_type: str, data: Any):
    """
    Method responsible for posting an event to a specific group of subscribers (event type)
    :param event_type: The identifier of the event
    :param data: The data to be passed to the subscribers
    :return:
    """

    if event_type not in subscribers:
        return
    for subscriber in subscribers[event_type]:
        subscriber(data)