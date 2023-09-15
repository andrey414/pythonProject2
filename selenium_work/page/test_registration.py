import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium_work.page.main_page import MainPage
from selenium_work.page.registration_form_page import RegistrationFormPage
import time


class TestBase:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.session = requests.Session()
        self.main_page = MainPage(self.driver)
        self.registration_form_page = RegistrationFormPage(self.driver)
        self.driver.implicitly_wait(3)
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


    def teardown_metod(self):
        self.driver.close()

class TestRegistration(TestBase):

    def setup_class(self):
        self.session = requests.Session()
        self.user_email = "aaandwefwfdreeyaddaywefw51kurochkin@gmail.com"
        self.user_password = "Qwerty123"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_metod(self):
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signup",json = self.user_to_login)
        self.session.delete(url="https://qauto2.forstudy.space/api/users",json = self.user_to_login)
        self.driver.quit()

    def test_registrarion_test(self):
        self.main_page.sign_up_button().click()
        self.registration_form_page.name_field().send_keys("test")
        self.registration_form_page.last_name_field().send_keys("lastnametest")
        self.registration_form_page.email_field().send_keys(self.user_email)
        self.registration_form_page.password_field().send_keys(self.user_password)
        self.registration_form_page.reenter_password_field().send_keys(self.user_password)
        self.registration_form_page.register_button().click()
        empty_garage = self.driver.find_elements(By.XPATH,"//p[text()='You don’t have any cars in your garage']")
        assert len(empty_garage) != 0


