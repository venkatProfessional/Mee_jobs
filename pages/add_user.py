import os
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import XLutility

class AddUser(BasePage):
    def __init__(self):
        super().__init__()

    def automate_add_user_page_navigation(self):
        try:
            self.driver.find_element(By.XPATH, "//span[@class='ms-2 d-none d-xl-inline-block user-item-desc']").click()
            self.driver.find_element(By.XPATH, "//a[@href='http://meejobs.itsfortesza.com/extra_user']").click()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Add User']").click()
            print("Navigation to Add User page successful.")
        except NoSuchElementException as e:
            print(f"Navigation element not found: {e}")
        except WebDriverException as e:
            print(f"WebDriver error during navigation: {e}")

    def export_from_excel_and_add_users(self):
        print("Form filling started...")

        file_path = os.path.join("C:\\Users", "JothiVenkatajalapath", "Desktop", "Working_with_py", "Meejobs.xlsx")
        sheet_name = "Sheet2"

        try:
            rows = XLutility.getRowCount(file_path, sheet_name)
            print(f"Number of rows found: {rows}")
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return

        for r in range(2, rows + 1):
            try:
                name = XLutility.readData(file_path, sheet_name, r, 1)
                email = XLutility.readData(file_path, sheet_name, r, 2)
                password = XLutility.readData(file_path, sheet_name, r, 3)
                role = XLutility.readData(file_path, sheet_name, r, 4)

                if None in [name, email, password, role]:
                    print(f"❗ Skipping row {r} due to missing data.")
                    continue

                # Fill the form
                self.driver.find_element(By.ID, "user_name").clear()
                self.driver.find_element(By.ID, "user_name").send_keys(name)

                self.driver.find_element(By.ID, "user_email").clear()
                self.driver.find_element(By.ID, "user_email").send_keys(email)

                self.driver.find_element(By.ID, "user_pswd").clear()
                self.driver.find_element(By.ID, "user_pswd").send_keys(password)

                self.driver.find_element(By.ID, "user_role").clear()
                self.driver.find_element(By.ID, "user_role").send_keys(role)

                # Click Save button
                self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
                print(f"✅ Successfully added user from row {r}.")

            except NoSuchElementException as e:
                print(f"❌ Element not found while filling row {r}: {e}")
            except WebDriverException as e:
                print(f"❌ WebDriver issue on row {r}: {e}")
            except Exception as e:
                print(f"❌ Unexpected error on row {r}: {e}")

