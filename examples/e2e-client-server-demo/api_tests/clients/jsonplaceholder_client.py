from __future__ import annotations

import requests


class JSONPlaceholderClient:
    """Thin wrapper around https://jsonplaceholder.typicode.com.

    JSONPlaceholder is the canonical free REST sandbox: full CRUD shape
    (POST/PUT/PATCH/DELETE simulate success and echo the payload), stable
    ids 1..10 for `/users`, and deterministic responses. Perfect for
    demonstrating the test patterns without needing real auth or tearing
    down state.
    """

    def __init__(self, base_url: str, session: requests.Session, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.session = session
        self.timeout = timeout

    def list_users(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/users", timeout=self.timeout)

    def get_user(self, user_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/users/{user_id}", timeout=self.timeout)

    def create_user(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/users", json=payload, timeout=self.timeout)

    def update_user(self, user_id: int, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}/users/{user_id}", json=payload, timeout=self.timeout)

    def patch_user(self, user_id: int, payload: dict) -> requests.Response:
        return self.session.patch(f"{self.base_url}/users/{user_id}", json=payload, timeout=self.timeout)

    def delete_user(self, user_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/users/{user_id}", timeout=self.timeout)

    def list_posts_for_user(self, user_id: int) -> requests.Response:
        return self.session.get(
            f"{self.base_url}/posts",
            params={"userId": user_id},
            timeout=self.timeout,
        )
