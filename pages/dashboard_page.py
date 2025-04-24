from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    MENU_ORDERS = (By.ID, "menu.orders")
    NEW_ORDER = (By.ID, "menu.new_order")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_order_page(self):
        self.click(self.MENU_ORDERS)


    def go_to_new_order_page(self):
        self.click(self.NEW_ORDER)


