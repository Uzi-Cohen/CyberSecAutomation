from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from shared.config import Config


class BasePage:
    """Common helpers. Page-specific objects subclass this."""

    def __init__(self, driver: WebDriver, timeout: int = Config.DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = "") -> None:
        url = f"{Config.UI_BASE_URL}{path}"
        self.driver.get(url)

    def find_visible(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_into(self, locator, text: str) -> None:
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator) -> str:
        return self.find_visible(locator).text

    def is_visible(self, locator) -> bool:
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False
