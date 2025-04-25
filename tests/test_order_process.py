
from datetime import datetime
import os

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from utilities.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.order_page import OrderPage

@pytest.mark.usefixtures("driver")
class TestOrderProcess:

    def test_order_process(self, driver):
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.CLIENT_LOGIN, Config.CLIENT_PASS)
        dashboard_page = DashboardPage(driver)
        dashboard_page.go_to_order_page()
        dashboard_page.go_to_new_order_page()
        WebDriverWait(driver, 10).until(EC.url_contains("orders/create"))
        order_page = OrderPage(driver)

        order_page.select_product()

        order_page.set_quantity(5)

        order_page.click_add_product()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        order_page.select_delivery_type("Siège")

        order_page.select_agency("Agence Tunis")

        order_page.select_payment_on_delivery("À la livraison")

        order_page.place_order()

        message = order_page.is_order_successful()
        assert "succès" in message.text.lower()


        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join("screenshots", f"{timestamp}_success.png")
        driver.get_screenshot_as_file(screenshot_path)

