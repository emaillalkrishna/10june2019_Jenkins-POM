import time
from testdata.data import *
from pages.webgeneric import *


class JenkinLogin(JenkinsWebGeric):
    def __init__(self, driver):
        JenkinsWebGeric.__init__(self, driver)

        self.locate_un_by_name = "j_username"
        self.locate_pn_by_name = "j_password"
        self.locate_signin_button_by_name = "Submit"

        global wb
        wg = JenkinsWebGeric(driver)

    def enter_username(self):
        wb.enter_val("name", self.locate_un_by_name, UN)
        time.sleep(2)

    def enter_password(self):
        wb.enter_val("name", self.locate_pn_by_name, PW)
        time.sleep(2)

    def click_signinbutton(self):
        wb.click_button("name", self.locate_signin_button_by_name)
        time.sleep(5)
