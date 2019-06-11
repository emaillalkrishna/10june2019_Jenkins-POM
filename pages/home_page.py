from pages.webgeneric import *


class JenkinLogout(JenkinsWebGeric):
    def __init__(self, driver):
        JenkinsWebGeric.__init__(self, driver)

        self.locate_logout_button_by_xpath = "//*[text()='log out']"

        global wb
        wb = JenkinsWebGeric(driver)

    def click_on_logout(self):
        wb.click_button("xpath", self.locate_logout_button_by_xpath)
