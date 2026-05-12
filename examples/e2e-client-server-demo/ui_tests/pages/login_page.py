from selenium.webdriver.common.by import By

from ui_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    URL_PATH = "/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    LOGOUT = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def open(self) -> "LoginPage":
        super().open(self.URL_PATH)
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        self.type_into(self.USERNAME, username)
        self.type_into(self.PASSWORD, password)
        self.click(self.SUBMIT)
        return self

    def flash_message(self) -> str:
        return self.text_of(self.FLASH)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGOUT)
