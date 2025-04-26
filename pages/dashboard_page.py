from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self):
        super().__init__()

    def verify_dashboard(self):
        title = self.driver.title
        print("Dashboard title:", title)
