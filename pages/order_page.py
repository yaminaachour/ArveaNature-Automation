import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    #"slect prod
    PRODUCT_SEARCH_INPUT = (By.ID, "searchinput_products")
    PRODUCT_ITEM = (By.CSS_SELECTOR, ".products_view")


    #quantity
    QUANTITY_INPUT = (By.ID, "quantity")

    ADD_PRODUCT =(By.ID, "add")

    EMPTY_CART_BUTTON = (By.ID, "clear-cart")
    NAME_NET_TO_PAY = (By.ID, "name_net_to_pay")

    TOTAL_NET_PAYABLE_LABEL = (By.ID, "name_net_to_pay")

    # Locators
    # Locators existants...
    DELIVERY_TYPE_DROPDOWN = (By.ID, "addDeliveryType")
    SELECT_DELIVERY_CONTAINER = (By.CSS_SELECTOR, "span[aria-labelledby='select2-addDeliveryType-container']")
    SELECT_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "ul.select2-results__options li")

    # Locators
    AGENCY_DROPDOWN = (By.CSS_SELECTOR, "span.select2-selection[aria-labelledby='select2-addDepot-container']")
    AGENCY_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and normalize-space()='{}']")
    AGENCY_SEARCH_INPUT = (By.CSS_SELECTOR, "input.select2-search__field")

    # Locators pour le mode de paiement

    PAYMENT_SELECT2_CONTAINER = (By.CSS_SELECTOR,
                                 "span.select2-selection[aria-labelledby='select2-paymentMode-container']")

    PAYMENT_SEARCH_INPUT = (By.XPATH, "//input[@aria-controls='select2-paymentMode-results']")


    ORDER_BUTTON = (By.ID, "saveOrderBtn")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "swal-modal")

    MSG_AGENCY_ERROR = (By.ID, "addDepot-error")
    MSG_PAYMENT_ERROR = (By.ID, "paymentMode-error")

    def __init__(self, driver):
        super().__init__(driver)


    def select_product(self):
            # Champ de recherche
            search_field = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_SEARCH_INPUT))
            search_field.click()
            time.sleep(1)
            # Attendre que la liste apparaisse
            self.wait.until(EC.presence_of_element_located((By.ID, "searchResults_products")))
            time.sleep(2)
            # Attendre qu'au moins un résultat soit cliquable
            self.wait.until(EC.element_to_be_clickable(self.PRODUCT_ITEM)).click()



    def set_quantity(self, quantity):
        quantity_input = self.wait.until(EC.element_to_be_clickable(self.QUANTITY_INPUT))
        # Effacer la valeur existante (si nécessaire)
        quantity_input.clear()
        # Taper la quantité souhaitée
        quantity_input.send_keys(str(quantity))

    def click_add_product(self):
        # Attendre que le bouton "Ajouter" soit cliquable
        add_button = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT))
        # Cliquer sur le bouton pour ajouter le produit au panier
        add_button.click()


    def is_empty_cart_button_displayed(self):
        # Vérifie si le bouton "Vider le panier" est affiché à l’écran
        return self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_BUTTON)).is_displayed()

    def select_delivery_type(self, option_text):
        """
        Sélectionne un type de livraison dans le menu déroulant Select2
        Args:
            option_text (str): Texte de l'option à sélectionner ("Transporteur" ou "Siège")
        """
        # 1. Cliquer pour ouvrir le dropdown Select2
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DELIVERY_CONTAINER)).click()

        # 2. Attendre que les options soient chargées
        self.wait.until(EC.visibility_of_element_located(self.SELECT_DROPDOWN_OPTIONS))

        # 3. Trouver et cliquer sur l'option souhaitée
        option_locator = (By.XPATH, f"//li[contains(text(), '{option_text}')]")
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()


    def get_selected_delivery_text(self):
        """Retourne le texte de l'option de livraison sélectionnée"""
        return self.wait.until(
            EC.visibility_of_element_located(self.SELECT_DELIVERY_CONTAINER)
        ).text

    def select_agency(self, agency_name="Agence Tunis"):

            # 1. Cliquer pour ouvrir le dropdown
            self.wait.until( EC.element_to_be_clickable(self.AGENCY_DROPDOWN)
            ).click()

            # 2. Attendre que le champ de recherche soit visible et saisir le texte
            search_input = self.wait.until( EC.visibility_of_element_located(self.AGENCY_SEARCH_INPUT)
            )
            search_input.send_keys(agency_name)

            # 3. Sélectionner l'option exacte
            self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[normalize-space()='{agency_name}']"))).click()

    def select_payment_on_delivery(self,payment_name):
        # 1. Ouvrir le dropdown
        dropdown = self.wait.until(EC.element_to_be_clickable(self.PAYMENT_SELECT2_CONTAINER))
        dropdown.click()
        # 2. Attendre que le champ de recherche s'affiche et y écrire la valeur
        input_field = self.wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@aria-controls='select2-paymentMode-results']")))
        input_field.send_keys(payment_name)
        # 3. Valider avec Entrée pour sélectionner l'option
        input_field.send_keys(Keys.ENTER)

    def is_total_net_payable_text_present(self):
        # Vérifie que le texte "Total net à payer" est présent dans l'élément
        total_text = self.wait.until(EC.visibility_of_element_located(self.TOTAL_NET_PAYABLE_LABEL)).text
        return "Total net à payer" in total_text








    def place_order(self):
        self.click(self.ORDER_BUTTON)

    def is_order_successful(self):
        # Attendre que le message de succès apparaisse
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

    def is_agency_error_displayed(self):
        # Attendre que le message d'erreur de l'agence soit visible
        error_message_agency = self.wait.until(EC.visibility_of_element_located(self.MSG_AGENCY_ERROR))
        # Vérifier si le message d'erreur est affiché
        return error_message_agency.is_displayed()

    def is_payment_mode_error_displayed(self):
        # Attendre que le message d'erreur soit visible
        error_message_payment = self.wait.until(EC.visibility_of_element_located(self.MSG_PAYMENT_ERROR))
        # Vérifier si le message d'erreur est affiché
        return error_message_payment.is_displayed()
