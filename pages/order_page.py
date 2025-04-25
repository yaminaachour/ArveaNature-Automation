import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    PRODUCT_SEARCH_INPUT = (By.ID, "searchinput_products")
    PRODUCT_ITEM = (By.XPATH, "//*[@id='searchResults_products']/div[1]")

    QUANTITY_INPUT = (By.ID, "quantity")

    ADD_PRODUCT =(By.ID, "add")

    EMPTY_CART_BUTTON = (By.ID, "clear-cart")
    NAME_NET_TO_PAY = (By.ID, "name_net_to_pay")

    TOTAL_NET_PAYABLE_LABEL = (By.ID, "name_net_to_pay")

    DELIVERY_TYPE_DROPDOWN = (By.ID, "addDeliveryType")
    SELECT_DELIVERY_CONTAINER = (By.CSS_SELECTOR, "span[aria-labelledby='select2-addDeliveryType-container']")
    SELECT_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "ul.select2-results__options li")

    AGENCY_DROPDOWN = (By.CSS_SELECTOR, "span.select2-selection[aria-labelledby='select2-addDepot-container']")
    AGENCY_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and normalize-space()='{}']")
    AGENCY_SEARCH_INPUT = (By.CSS_SELECTOR, "input.select2-search__field")

    PAYMENT_SELECT2_CONTAINER = (By.CSS_SELECTOR,"span.select2-selection[aria-labelledby='select2-paymentMode-container']")

    PAYMENT_SEARCH_INPUT = (By.XPATH, "//input[@aria-controls='select2-paymentMode-results']")


    ORDER_BUTTON = (By.ID, "saveOrderBtn")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "swal-modal")

    MSG_AGENCY_ERROR = (By.ID, "addDepot-error")
    MSG_PAYMENT_ERROR = (By.ID, "paymentMode-error")

    def __init__(self, driver):
        super().__init__(driver)


    def select_product(self):
        search_field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_SEARCH_INPUT))
        search_field.click()
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_SEARCH_INPUT))
        time.sleep(2)
        product =self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='products_view' and contains(@data-product, 'Savon Argan')]")))
        product.click()

    def set_quantity(self, quantity):
        quantity_input = self.wait.until(EC.element_to_be_clickable(self.QUANTITY_INPUT))
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

    def click_add_product(self):
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT))
        add_button.click()


    def is_empty_cart_button_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_BUTTON)).is_displayed()

    def select_delivery_type(self, option_text):

        self.wait.until(EC.element_to_be_clickable(self.SELECT_DELIVERY_CONTAINER)).click()
        self.wait.until(EC.visibility_of_element_located(self.SELECT_DROPDOWN_OPTIONS))
        option_locator = (By.XPATH, f"//li[contains(text(), '{option_text}')]")
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()


    def get_selected_delivery_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SELECT_DELIVERY_CONTAINER)).text

    def select_agency(self, agency_name="Agence Tunis"):
            self.wait.until( EC.element_to_be_clickable(self.AGENCY_DROPDOWN) ).click()
            search_input = self.wait.until( EC.visibility_of_element_located(self.AGENCY_SEARCH_INPUT) )
            search_input.send_keys(agency_name)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space()='{agency_name}']"))).click()

    def select_payment_on_delivery(self,payment_name):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_SELECT2_CONTAINER))
        dropdown.click()
        input_field = self.wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@aria-controls='select2-paymentMode-results']")))
        input_field.send_keys(payment_name)
        input_field.send_keys(Keys.ENTER)


    def place_order(self):
        self.click(self.ORDER_BUTTON)

    def is_order_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

