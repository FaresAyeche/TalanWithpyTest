from selenium import webdriver


from Config1.config import TestData
from TEST1.test_base import BaseTest
from pages.connexionPage import connexion
class Test_connexion(BaseTest):

    def test_valid_connexion(self):

        self.cx = connexion(self.driver)
        self.cx.acceder_connexion_page()
        self.cx.remplissage_log(TestData.email, TestData.mdp)
        self.cx.clique_SE_Connecter()
        b = self.cx.have_text()
        print(b)
        assert self.cx.verif_url(TestData.url_page_dashboard)
        assert b == "Bienvenue Fares!"


    def test_email_non_valid_connexion(self):

        self.cx = connexion(self.driver)
        self.cx.acceder_connexion_page()
        self.cx.remplissage_log(TestData.emailNV, TestData.mdp)
        self.cx.clique_SE_Connecter()
        assert self.cx.verif_url(TestData.url_page_login)


    def test_mdp_non_valid_connexion(self):

        self.cx = connexion(self.driver)
        self.cx.acceder_connexion_page()
        self.cx.remplissage_log(TestData.email, TestData.mdpNV)
        self.cx.clique_SE_Connecter()
        assert self.cx.verif_url(TestData.url_page_login)

