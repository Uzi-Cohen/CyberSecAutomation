"""Offline smoke tests — no network. Useful as a CI canary and to verify the
framework wiring (schema loading, parametrization, data factory) without
depending on any external service."""
import json
from pathlib import Path

import pytest
from jsonschema import ValidationError, validate

from shared.data_factory import new_user_payload, random_email

pytestmark = [pytest.mark.api]

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "user.schema.json"
FIXTURE = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {"lat": "-37.3159", "lng": "81.1496"},
    },
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets",
    },
}


@pytest.fixture(scope="module")
def user_schema():
    return json.loads(SCHEMA_PATH.read_text())


def test_valid_fixture_passes_schema(user_schema):
    validate(instance=FIXTURE, schema=user_schema)


def test_missing_required_field_fails_schema(user_schema):
    bad = {**FIXTURE}
    del bad["email"]
    with pytest.raises(ValidationError):
        validate(instance=bad, schema=user_schema)


def test_wrong_type_fails_schema(user_schema):
    bad = {**FIXTURE, "id": "not-an-int"}
    with pytest.raises(ValidationError):
        validate(instance=bad, schema=user_schema)


def test_invalid_email_fails_schema(user_schema):
    from jsonschema import Draft7Validator, FormatChecker

    bad = {**FIXTURE, "email": "not-an-email"}
    validator = Draft7Validator(user_schema, format_checker=FormatChecker())
    errors = list(validator.iter_errors(bad))
    assert any("email" in str(err.path) or "format" in err.message for err in errors)


def test_data_factory_produces_unique_payloads():
    a = new_user_payload()
    b = new_user_payload()
    assert a["name"] != b["name"]
    assert a["job"] == "qa-automation-engineer"


def test_random_email_has_expected_shape():
    email = random_email(prefix="alice")
    assert email.startswith("alice.")
    assert email.endswith("@example.com")
    assert "@" in email
