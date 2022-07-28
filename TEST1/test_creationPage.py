from urllib3.util import url

from Config1.config import TestData
from TEST1.test_base import BaseTest
from pages.creationPage import creation_Page
class Test_crea(BaseTest):

    def test_acces_inscri(self):

        self.cp = creation_Page(self.driver)
        assert self.cp.verif_url(TestData.b)
        self.cp.acceder_inscri_page()

    def test_remplissage_champs(self):
        self.cp = creation_Page(self.driver)
        self.cp.remplissage_nom(TestData.nom, TestData.prenom, TestData.email, TestData.mdp, TestData.cmdp)

