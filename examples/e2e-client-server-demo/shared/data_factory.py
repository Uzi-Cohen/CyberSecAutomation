import random
import string


def random_email(prefix: str = "qa") -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{prefix}.{suffix}@example.com"


def random_name() -> str:
    return "".join(random.choices(string.ascii_letters, k=10))


def new_user_payload(**overrides) -> dict:
    payload = {"name": random_name(), "job": "qa-automation-engineer"}
    payload.update(overrides)
    return payload
