from Config1.config import TestData
from TEST1.test_base import BaseTest
from pages.connexionPage import connexion
from pages.changementNumPage import changementNum


class Test_connexion(BaseTest):

    def test_changement_numValid(self):
        self.chn = changementNum(self.driver)
        self.cx = connexion(self.driver)
        self.cx.acceder_connexion_page()
        self.cx.remplissage_log(TestData.email, TestData.mdp)
        self.cx.clique_SE_Connecter()
        b = self.cx.have_text()
        print(b)
        assert self.cx.verif_url(TestData.url_page_dashboard)
        assert b == "Bienvenue Fares!"
        self.chn.acceder_profil_page()
        self.chn.vider_champ_tel()
        self.chn.remplissage_champ_tel(TestData.telValid)
        self.chn.cliquer_sauvgarder_changement()
        assert self.chn.verif_enregistrement()

    def test_changement_numNonValid(self):
        self.chn = changementNum(self.driver)
        self.cx = connexion(self.driver)
        self.cx.acceder_connexion_page()
        self.cx.remplissage_log(TestData.email, TestData.mdp)
        self.cx.clique_SE_Connecter()
        b = self.cx.have_text()
        print(b)
        assert self.cx.verif_url(TestData.url_page_dashboard)
        assert b == "Bienvenue Fares!"
        self.chn.acceder_profil_page()
        self.chn.vider_champ_tel()
        self.chn.remplissage_champ_tel(TestData.telNonValid)
        self.chn.cliquer_sauvgarder_changement()
        assert self.chn.verif_nonEnregistrement()
