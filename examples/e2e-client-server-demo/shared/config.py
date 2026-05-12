import os


class Config:
    API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
    UI_BASE_URL = os.getenv("UI_BASE_URL", "https://the-internet.herokuapp.com")

    UI_USERNAME = os.getenv("UI_USERNAME", "tomsmith")
    UI_PASSWORD = os.getenv("UI_PASSWORD", "SuperSecretPassword!")

    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
    HTTP_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "10"))
