import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

s = Service(r'\Presta-Forfiter-master\Presta-Forfiter-master\selenium_tests\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://localhost:8080")

class PrestaShopTests:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/index.php")
        self.driver.set_window_size(1294, 1440)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#category-5 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "ANGEL\'S ENVY PORT FINISH...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.LINK_TEXT, "BAKER\'S 7YO BOURBON 0,7L 53,5%").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-29 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "ABERFELDY 12YO THE GOLDEN...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-32 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "BALLANTINE\'S 21YO WHISKY...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-38 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "CHIVAS REGAL 12YO WHISKY...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-38 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(7) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-67 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "GRANT\'S WHISKY 40%").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.find_element(By.CSS_SELECTOR, "#category-9 > .dropdown-item").click()
        self.driver.find_element(By.LINK_TEXT, "CHOPIN TRIBUTE EDITION...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        pass

    def test_search_and_add_to_cart(self):
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("chopin tribute edition")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "CZĘSTOCHÓWKA MALINA Z...").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        pass

    def test_delete_from_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".cart-products-count").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(3) .col-md-2 .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(7) .col-md-2 .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(9) .col-md-2 .material-icons").click()
        pass

    def test_registration(self):
        self.driver.find_element(By.CSS_SELECTOR, ".user-info .hidden-sm-down").click()
        self.driver.find_element(By.LINK_TEXT, "Nie masz konta? Załóż je tutaj").click()
        self.driver.find_element(By.ID, "field-id_gender-2").click()
        self.driver.find_element(By.ID, "field-firstname").click()
        self.driver.find_element(By.ID, "field-firstname").send_keys("Marta")
        self.driver.find_element(By.ID, "field-lastname").click()
        self.driver.find_element(By.ID, "field-lastname").send_keys("Lee")
        self.driver.find_element(By.ID, "field-email").click()
        self.driver.find_element(By.ID, "field-email").send_keys("martale@gmail.com")
        self.driver.find_element(By.ID, "field-password").click()
        self.driver.find_element(By.ID, "field-password").send_keys("12345678A")
        self.driver.find_element(By.ID, "field-birthday").click()
        self.driver.find_element(By.ID, "field-birthday").send_keys("1999-05-01")
        self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
        self.driver.find_element(By.NAME, "customer_privacy").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
        self.driver.find_element(By.NAME, "psgdpr").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
    pass

    def test_buy_from_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".header > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        self.driver.find_element(By.ID, "field-address1").click()
        self.driver.find_element(By.ID, "field-address1").send_keys("Traugutta")
        self.driver.find_element(By.ID, "field-address2").click()
        self.driver.find_element(By.ID, "field-address2").send_keys("100")
        self.driver.find_element(By.ID, "field-postcode").click()
        self.driver.find_element(By.ID, "field-postcode").click()
        self.driver.find_element(By.ID, "field-postcode").send_keys("80-226")
        self.driver.find_element(By.ID, "field-city").click()
        self.driver.find_element(By.ID, "field-city").send_keys("Gdansk")
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        pass

    def test_order_status(self):
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.find_element(By.CSS_SELECTOR, "#history-link .material-icons").click()
        self.driver.find_element(By.LINK_TEXT, "Zamówienia").click()
        pass

    def run_tests(self):
        self.setUp()
        try:
            self.test_add_to_cart()
            self.test_search_and_add_to_cart()
            self.test_delete_from_cart()
            self.test_registration()
            self.test_buy_from_cart()
            self.test_order_status()
        finally:
            self.tearDown()

if __name__ == "__main__":
    test_suite = PrestaShopTests()
    test_suite.run_tests()
