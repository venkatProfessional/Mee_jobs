from selenium.webdriver.common.by import By

from selenium_helper.common_code import CommonCode

class BasePage:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("http://meejobs.itsfortesza.com/")
        self.login()

    def login(self):
        try:
            self.driver.find_element(By.ID, "email").send_keys("begata6168@f5url.com")
            self.driver.find_element(By.ID, "password").send_keys("Dinesh@123")
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            self.helper.wait()
            print("Login successful.")
        except Exception as e:
            print(f"Login failed: {e}")
