from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Adduser(BasePage):
    def __init__(self):
        super().__init__()

    def AutomateAdduser(self):
        self.driver.find_element(By.XPATH,"//span[@class='ms-2 d-none d-xl-inline-block user-item-desc']").click()
        self.driver.find_element(By.XPATH,"//a[@href='http://meejobs.itsfortesza.com/extra_user']").click()


