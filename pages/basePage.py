from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import url


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def clique(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def remplissage(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    def avoir_text(self, by_locator):
       element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
       return element.text
    def visible(self, by_locator):
       element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
       return bool(element)
    def verif_url(self,text):
        element = WebDriverWait(self.driver, 10).until(EC.url_contains(text))
        return bool(element)
    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
