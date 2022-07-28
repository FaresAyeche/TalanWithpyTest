import pytest
from selenium import webdriver

from Config1.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_executable_path)

    request.cls.driver = web_driver
    web_driver.maximize_window()

    web_driver.implicitly_wait(10)
    #yield
    #web_driver.close()
