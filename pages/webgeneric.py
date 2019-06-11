
from pages.locgeneric import *

class JenkinsWebGeric(JenkinLocGeneric):
    def __init__(self, driver):
        JenkinLocGeneric.__init__(self, driver)

        global loc
        loc = JenkinLocGeneric(driver)

    def enter_val(self, loc_type, loc_value, data):
        loc.locator(loc_type,loc_value).send_keys(data)


    def click_button(self, loc_type, loc_value):
        loc.locator(loc_type,loc_value).click()



