import json
from pathlib import Path

import pytest
from jsonschema import validate

pytestmark = [pytest.mark.api]

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "user.schema.json"


@pytest.fixture(scope="module")
def user_schema():
    return json.loads(SCHEMA_PATH.read_text())


def test_single_user_response_matches_schema(api, user_schema):
    response = api.get_user(user_id=1)
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)


@pytest.mark.parametrize("user_id", [1, 2, 3, 7, 10])
def test_schema_holds_across_known_users(api, user_id, user_schema):
    response = api.get_user(user_id=user_id)
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)


def test_list_users_items_all_match_schema(api, user_schema):
    response = api.list_users()
    assert response.status_code == 200
    for user in response.json():
        validate(instance=user, schema=user_schema)
