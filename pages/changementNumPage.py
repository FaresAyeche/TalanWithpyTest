from selenium.webdriver.common.by import By

from Config1.config import TestData
from pages.basePage import BasePage


class changementNum(BasePage):
    btn_profil = (By.ID, "userAccount")
    btn_profil_2 = (By.XPATH, "//*[@id='menu']/div/div/div/div/h4/span/span/a[1]")
    btn_affiche_btn = (By.ID, "fa-angle-main-nav")
    champ = (By.ID, "student_tel")
    btn_enregistrer = (By.ID, "student_save")
    done = (By.XPATH, "//*[@id='body']/div[4]/div/div[2]")
    NOK = (By.XPATH, "//*[@id='student_tel-error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        driver.get(TestData.base_url)

    def acceder_profil_page(self):

        self.clique(self.btn_affiche_btn)
        self.clique(self.btn_profil)
        self.clique(self.btn_profil_2)

    def vider_champ_tel(self):
        self.clear(self.champ)

    def remplissage_champ_tel(self, num):
        self.remplissage(self.champ, num)

    def cliquer_sauvgarder_changement(self):
        self.clique(self.btn_enregistrer)

    def verif_enregistrement(self):
        return self.visible(self.done)

    def verif_nonEnregistrement(self):
        return self.visible(self.NOK)
