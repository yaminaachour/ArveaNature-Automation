import pytest

from pages.login_page import LoginPage
from utilities.config import Config
import allure


@pytest.mark.usefixtures("driver")
class TestLogin:

    @allure.step("Test login success")
    def test_login_success(self, driver):
        with allure.step("1. HTTP Authentication"):
            driver.get(Config.BASE_URL)

        with allure.step("2. Login via form"):
            login_page = LoginPage(driver)
            login_page.login(Config.CLIENT_LOGIN, Config.CLIENT_PASS)

        with allure.step("3. Verify login success"):
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            assert "Dashboard" in driver.title
