from selenium.webdriver.common.by import By

from Config1.config import TestData
from pages.basePage import BasePage


class creation_Page(BasePage):
    btn_inscri = (By.XPATH, "//*[@id='main-menu']/div/div/div/nav/div/ul/li[6]/a")
    champ_nom = (By.ID, "user_lastName")
    champ_prenom = (By.ID,"user_firstName")
    champ_email = (By.ID, "user_email")
    champ_confirmation_mdp = (By.ID, "user_password_first")
    champ_mdp = (By.ID, "user_password_second")
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get(TestData.base_url)
    
    


    def acceder_inscri_page(self):
        self.clique(self.btn_inscri)
    def remplissage_nom(self, nom, prenom, email, mdp , cmdp):
        self.remplissage(self.champ_nom, nom)
        self.remplissage(self.champ_prenom, prenom)
        self.remplissage(self.champ_email, email)
        self.remplissage(self.champ_mdp, mdp)
        self.remplissage(self.champ_confirmation_mdp, cmdp)
    #def verif_current_url(self,text):
     #   return self.verif_url(self,TestData.b)



