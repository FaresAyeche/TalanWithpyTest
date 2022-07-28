from selenium.webdriver.common.by import By

from Config1.config import TestData
from pages.basePage import BasePage


class connexion(BasePage):
    btn_connexion = (By.XPATH, "//*[@id='main-menu']/div/div/div/nav/div/ul/li[5]/a")
    btn_SE_CONNECTER = (By.XPATH, "//*[@id='myModal']/div/div/div[3]/form/div[3]/button")
    champ_email2 = (By.ID, "inputEmail")
    champ_mdp2 = (By.ID, "inputPassword")
    titre = (By.XPATH, "//*[@id='body']/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get(TestData.base_url)

    def acceder_connexion_page(self):
        self.clique(self.btn_connexion)

    def remplissage_log(self, email, mdp):
        self.remplissage(self.champ_email2, email)
        self.remplissage(self.champ_mdp2, mdp)

    def clique_SE_Connecter(self):
        self.clique(self.btn_SE_CONNECTER)

    def have_text(self):
        return self.avoir_text(self.titre)
