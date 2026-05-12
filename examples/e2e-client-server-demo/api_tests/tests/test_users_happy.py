import pytest

from shared.data_factory import new_user_payload

pytestmark = [pytest.mark.api]


@pytest.mark.smoke
def test_list_users_returns_200_and_ten_users(api):
    response = api.list_users()
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 10


def test_get_existing_user_returns_200(api):
    response = api.get_user(user_id=2)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 2
    assert body["username"]
    assert "@" in body["email"]


def test_create_user_returns_201_and_echoes_payload(api):
    payload = new_user_payload(name="Alice", job="qa-automation")
    response = api.create_user(payload)
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Alice"
    assert body["job"] == "qa-automation"
    assert "id" in body


def test_update_user_returns_200_and_full_replacement(api):
    payload = {"name": "Bob", "username": "bob42", "email": "bob@example.com"}
    response = api.update_user(user_id=2, payload=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Bob"
    assert body["id"] == 2


def test_patch_user_returns_200_with_merged_fields(api):
    response = api.patch_user(user_id=2, payload={"name": "Charlie"})
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Charlie"
    assert body["id"] == 2


def test_delete_user_returns_200(api):
    response = api.delete_user(user_id=2)
    assert response.status_code == 200


def test_list_posts_filtered_by_user_returns_only_that_user(api):
    response = api.list_posts_for_user(user_id=1)
    assert response.status_code == 200
    posts = response.json()
    assert all(post["userId"] == 1 for post in posts)
    assert len(posts) > 0
