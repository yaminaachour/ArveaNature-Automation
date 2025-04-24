
import time
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



        # Login
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        login_page.login(Config.CLIENT_LOGIN, Config.CLIENT_PASS)
        time.sleep(1)
        # Naviguer vers la page de commande
        dashboard_page = DashboardPage(driver)
        time.sleep(1)
        dashboard_page.go_to_order_page()
        time.sleep(1)
        dashboard_page.go_to_new_order_page()

        time.sleep(1)
        # Vérification de l'URL actuelle pour s'assurer que nous sommes bien sur la page souhaitée
        WebDriverWait(driver, 10).until(EC.url_contains("orders/create"))
        time.sleep(5)
        # Étape 3: Ajouter un produit dans le panier

        order_page = OrderPage(driver)

        order_page.select_product()
        driver.implicitly_wait(7)


        # Étape 4: Ajuster la quantité à 5
        order_page.set_quantity(5)
        time.sleep(1)


        order_page.click_add_product()
        # Attendre un peu que l'action soit effectuée
        driver.implicitly_wait(3)

        # Faire défiler la page vers le bas
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Étape 5: Sélectionner le mode de livraison “Siège”


            # Sélectionner "Siège" comme mode de livraison
        order_page.select_delivery_type("Siège")

            # Vérifier la sélection

    # Étape 6: Choisir le siège “Agence Tunis”


        order_page.select_agency("Agence Tunis")

        # Étape 7: Sélectionner le mode de paiement “À la livraison”
        order_page.select_payment_on_delivery("À la livraison")

        # Étape 8: Cliquer sur “Commander”
        order_page.place_order()

         #verfication
        message = order_page.is_order_successful()
        assert "succès" in message.text.lower()