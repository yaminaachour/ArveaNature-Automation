import pytest
import time
from pages.login_page import LoginPage
from utilities.config import Config
import allure

@pytest.mark.usefixtures("driver")
class TestLogin:

    @allure.step("Test de connexion complète (HTTP + formulaire)")
    def test_login_success(self, driver):
        # Étape 1 : Authentification HTTP
        with allure.step("1. Authentification HTTP"):
            driver.get(Config.BASE_URL)

        time.sleep(4)

        # Étape 2 : Remplir formulaire utilisateur
        with allure.step("2. Connexion via formulaire"):
            login_page = LoginPage(driver)
            login_page.login(Config.CLIENT_LOGIN, Config.CLIENT_PASS)
            time.sleep(1)

        # Étape 3 : Vérification
        with allure.step("3. Vérifier la connexion"):
            print("URL actuelle:", driver.current_url)
            print("Titre de la page:", driver.title)
            assert "Dashboard" in driver.title
