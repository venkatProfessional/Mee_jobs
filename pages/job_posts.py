import os
from selenium.webdriver.support.ui import Select
from selenium_helper.common_code import CommonCode
from utils import XLutility
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class AutomateJobposts:
    def __init__(self):
        self.helper = CommonCode()
        self.driver = self.helper.driver
        self.helper.open_url("http://meejobs.itsfortesza.com/")

    def login(self):
        try:
            Email = self.driver.find_element(By.XPATH, "//input[@id='email']")
            Email.send_keys("begata6168@f5url.com")
            Password = self.driver.find_element(By.XPATH, "//input[@id='password']")
            Password.send_keys("Dinesh@123")
            loginbtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
            loginbtn.click()
            self.helper.wait()

            title = self.driver.title
            print(title)
            if "Employer Dashboard |Cherrypix" in title:
                print("Login passed")
            else:
                print("Login failed.")

            self.navigate_to_post_job_tab()

        except Exception as e:
            print(f"Error during login process: {e}")

    def navigate_to_post_job_tab(self):
        jobs = self.driver.find_element(By.XPATH, "//span[normalize-space()='Jobs']")
        jobs.click()
        self.helper.wait()
        postjob = self.driver.find_element(By.XPATH, "//a[@id='post-job-tab']")
        postjob.click()
        self.helper.wait(5)

    def fillformfields(self):
        print("Fill form started")
        file = os.path.join("C:\\Users", "JothiVenkatajalapath", "Desktop", "Working_with_py", "Meejobs.xlsx")

        try:
            rows = XLutility.getRowCount(file, "Sheet1")
            print("The rows count is:", rows)
        except Exception as e:
            print(f"Error reading Excel: {e}")
            return

        for r in range(2, rows + 1):
            try:
                JobTitle = XLutility.readData(file, "Sheet1", r, 1)
                JobDescription = XLutility.readData(file, "Sheet1", r, 2)
                RolesandResponsibilities = XLutility.readData(file, "Sheet1", r, 3)
                JobMode = XLutility.readData(file, "Sheet1", r, 4)
                Skills = XLutility.readData(file, "Sheet1", r, 5)
                relevingDuration = XLutility.readData(file, "Sheet1", r, 6)
                Qualification = XLutility.readData(file, "Sheet1", r, 7)
                Experience = XLutility.readData(file, "Sheet1", r, 8)
                JobLocation = XLutility.readData(file, "Sheet1", r, 9)
                Salaryfrom = XLutility.readData(file, "Sheet1", r, 10)
                Salaryto = XLutility.readData(file, "Sheet1", r, 11)

                if None in [JobTitle, JobDescription, RolesandResponsibilities, JobMode, Skills, relevingDuration, Qualification, Experience, Salaryfrom, Salaryto]:
                    print(f"\n❗ Row {r} has missing data. Skipping.")
                    continue

                self.driver.find_element(By.ID, "job_title").send_keys(JobTitle)
                self.driver.find_element(By.ID, "job_desc").send_keys(JobDescription)
                self.driver.find_element(By.ID, "roles_responsebility").send_keys(RolesandResponsibilities)
                self.driver.find_element(By.ID, "job_mode").send_keys(JobMode)
                self.driver.find_element(By.ID, "secondary_skills").send_keys(Skills)
                self.driver.find_element(By.ID, "join_duration_from").send_keys("28-06-2025")
                self.driver.find_element(By.ID, "join_duration_to").send_keys("29-08-2025")
                self.driver.find_element(By.ID, "educational_qualify").send_keys(Qualification)

                Select(self.driver.find_element(By.ID, "tot_year_exp_from")).select_by_visible_text("1")
                Select(self.driver.find_element(By.ID, "tot_year_exp_to")).select_by_visible_text("5")

                self.driver.find_element(By.ID, "job_location").send_keys(JobLocation)
                self.driver.find_element(By.ID, "salary_from").send_keys(Salaryfrom)
                self.driver.find_element(By.ID, "salary_to").send_keys(Salaryto)

                self.helper.wait()
                self.driver.find_element(By.XPATH, "//button[2]").click()
                self.helper.wait()

                # Refresh the page and navigate back to the post job form
                self.driver.refresh()
                self.helper.wait(3)
                self.navigate_to_post_job_tab()

            except NoSuchElementException as e:
                print(f"Element not found in row {r}: {e}")
            except WebDriverException as e:
                print(f"WebDriver error in row {r}: {e}")
            except Exception as e:
                print(f"Unexpected error in row {r}: {e}")

if __name__ == "__main__":
    test = AutomateJobposts()
    test.login()
    test.fillformfields()


# Dinesh@123