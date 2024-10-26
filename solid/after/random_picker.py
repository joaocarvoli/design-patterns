from typing import List, Any
import secrets

def choose_a_random_item(items: List[Any]) -> Any:
    if not items:
        raise ValueError("Cannot choose from an empty collection.")
    return secrets.choice(list(items))