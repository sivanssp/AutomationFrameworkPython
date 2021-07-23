import allure
import moment
from selenium import webdriver
import pytest
from pages.loginpage import loginpage
from pages.homePage import Homepage
from utils import utils as utils
from _ast import Assert

class Test_login():

    @pytest.mark.usefixtures("test_setup")
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    @pytest.mark.usefixtures("test_setup")
    def test_logout(self):
        try:
            driver = self.driver
            homepage = Homepage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            y = "abc"
            assert x == y

        except AssertionError as error:
            print("Assert error occured")
            print(error)
            cur_time = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            test_name=utils.whoami()
            screenshot_name = test_name+"_"+cur_time
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("F:/AutomationFrameworkPython/screenshots/"+screenshot_name+".png")
            raise
        except:
            print("there was an exception")
            cur_time = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + cur_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("F:/AutomationFrameworkPython/screenshots/" + screenshot_name + ".png")
            raise
        else:
            print("No exception occured")
        finally:
            print("i am inside the final block")








