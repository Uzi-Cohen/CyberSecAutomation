import pytest

pytestmark = [pytest.mark.api]


def test_get_unknown_user_returns_404(api):
    response = api.get_user(user_id=9999)
    assert response.status_code == 404
    assert response.json() == {}


def test_get_zero_user_returns_404(api):
    response = api.get_user(user_id=0)
    assert response.status_code == 404


@pytest.mark.parametrize("user_id", [11, 12, 100, 9999])
def test_get_out_of_range_user_returns_404(api, user_id):
    response = api.get_user(user_id=user_id)
    assert response.status_code == 404


def test_list_posts_for_unknown_user_returns_empty_array(api):
    response = api.list_posts_for_user(user_id=9999)
    assert response.status_code == 200
    assert response.json() == []
