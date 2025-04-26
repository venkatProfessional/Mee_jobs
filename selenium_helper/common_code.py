import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class CommonCode:
    def __init__(self):
        """Initialize WebDriver with given driver path."""
        service_obj = Service(r"C:\drivers_selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_obj)

    def open_url(self, url, maximize=True, wait_time=2):
        """Opens a URL, maximizes the window, and waits."""
        self.driver.get(url)
        time.sleep(wait_time)
        if maximize:
            self.driver.maximize_window()
        time.sleep(wait_time)

    def close_browser(self):
        """Closes the browser."""
        self.driver.quit()

    @staticmethod
    def wait(seconds=2):
        """Static method to add a sleep wait."""
        time.sleep(seconds)

    def service_obj(self):
        pass


