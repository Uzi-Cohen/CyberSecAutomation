# Test Case Template

Each test case follows this structure. Concrete examples below.

```
ID: TC-<MODULE>-<NNN>
Title:
Module / feature:
Type: [API | UI | E2E | Smoke]
Priority: [P0 | P1 | P2]
Linked requirement: PRD-…
Linked automated test: <path>::<function>

Preconditions:
  - …

Test data:
  - …

Steps:
  1.
  2.
  3.

Expected result:
  - …

Postconditions / cleanup:
  - …
```

---

## Example: TC-USERMGMT-001 — Successful login

| Field | Value |
|---|---|
| ID | TC-USERMGMT-001 |
| Title | A valid user can log in and see the secure area |
| Module | Login |
| Type | UI (Smoke) |
| Priority | P0 |
| Linked requirement | PRD-USERMGMT-v3 §4.1 |
| Linked automated test | `ui_tests/tests/test_login.py::test_valid_login_lands_on_secure_area` |

**Preconditions**
- A user `tomsmith` with password `SuperSecretPassword!` exists.
- App is reachable at `UI_BASE_URL`.

**Test data**
- Username: `tomsmith`
- Password: `SuperSecretPassword!`

**Steps**
1. Open `/login`.
2. Enter username and password.
3. Click "Login".

**Expected result**
- Browser navigates to `/secure`.
- Logout button is visible.
- Flash message contains "You logged into a secure area".

**Postconditions**
- None (read-only test).

---

## Example: TC-USERMGMT-014 — E2E: API-created user is reflected in UI

| Field | Value |
|---|---|
| ID | TC-USERMGMT-014 |
| Title | A user record created via API is visible to a UI-authenticated session |
| Module | E2E |
| Type | E2E |
| Priority | P0 |
| Linked requirement | PRD-USERMGMT-v3 §6.2 (Client-Server data consistency) |
| Linked automated test | `ui_tests/tests/test_e2e_client_server.py::test_user_created_via_api_can_login_via_ui` |

**Preconditions**
- API and UI point at the same backend (in production).
- Test runner has network access to both.

**Test data**
- Generated via `shared.data_factory.new_user_payload()` — randomized name to avoid collisions.

**Steps**
1. POST a new user via the API; capture the returned `id`.
2. Open the UI login page.
3. Authenticate as a session user.
4. Verify the secure area loads.

**Expected result**
- API returns 201 with the echoed payload and an `id`.
- UI login succeeds.
- Secure area is rendered.

**Postconditions**
- API: delete the created user (cleanup) — skipped in the demo because the public sandbox is ephemeral.

---

## Example: TC-USERMGMT-021 — API: unknown user returns 404

| Field | Value |
|---|---|
| ID | TC-USERMGMT-021 |
| Title | GET /users/{id} for non-existent id returns 404 with empty body |
| Module | Users API |
| Type | API (Negative) |
| Priority | P1 |
| Linked requirement | API spec §3.2 error contracts |
| Linked automated test | `api_tests/tests/test_users_negative.py::test_get_unknown_user_returns_404` |

**Preconditions**
- API reachable.

**Test data**
- `user_id = 23` (sandbox guarantees this is not present).

**Steps**
1. GET `/users/23`.

**Expected result**
- Status 404.
- Response body is `{}`.

**Postconditions**
- None.
