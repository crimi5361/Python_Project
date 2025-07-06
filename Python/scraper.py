import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime

class Scraper:
    def __init__(self, logger, screenshot_dir="screenshots"):
        self.logger = logger
        self.screenshot_dir = screenshot_dir
        os.makedirs(screenshot_dir, exist_ok=True)

        # Configuration du navigateur Edge
        options = Options()
        options.add_argument('--headless')  # Mode sans interface graphique
        service = Service(r"C:\Users\IIPEA\Downloads\edgedriver_win32\msedgedriver.exe")  ##  telecharger le service de Edge ou chrome et installer le  puis copier le chemin ici "msedgedriver.exe""
        self.driver = webdriver.Edge(service=service, options=options)

    def login_and_capture(self, site, user, password):
        try:
            self.driver.get(site)
            time.sleep(2)

            # Détection automatique par attributs
            input_user = self.driver.find_element(By.XPATH, "//input[@type='text' or @name='username' or contains(@id, 'user')]")
            input_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
            input_user.send_keys(user)
            input_password.send_keys(password)

            # Tentative de soumission (form button)
            try:
                btn = self.driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Login') or contains(text(), 'Connexion')]")
                btn.click()
            except NoSuchElementException:
                input_password.submit()

            time.sleep(3)

            # Vérifier si on est connecté (par URL qui change ou élément visible)
            if "dashboard" in self.driver.current_url.lower() or "account" in self.driver.current_url.lower():
                self.take_screenshot(site, user)
                self.logger.log(site, user, 200, True)
            else:
                self.logger.log(site, user, 403, False)

        except Exception as e:
            print(f"Erreur lors de la connexion à {site} avec {user}: {e}")
            self.logger.log(site, user, 500, False)

    def take_screenshot(self, site, user):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        site_name = site.replace("https://", "").replace("http://", "").replace("/", "_")
        filename = f"{self.screenshot_dir}/{user}_{site_name}_{timestamp}.png"
        self.driver.save_screenshot(filename)

    def close(self):
        self.driver.quit()
