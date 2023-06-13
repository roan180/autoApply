
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class indeed:
    def __init__(self):
        #user_data_dir = r'C:\Users\ericb\AppData\Local\Google\Chrome\User Data' #gaming PC
        user_data_dir = r'Users/Eric Salazar/Library/Application Support/Google/Chrome' #laptop

        # Configure Chrome options
        options = Options()
        options.add_argument(f'--user-data-dir={user_data_dir}')

        # Create the ChromeDriver instance with the specified user data directory
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

        # locators for the job beacons and other info
        self.jobs_beacon = "//div[@class='job_seen_beacon']"
        self.jobs_beacon_a = "//a[contains(@class,'jcs-JobTitle')]"
        self.job_beacon_title = "//span[contains(@id,'jobTitle')]"
        self.job_beacon_company_name = "//span[@class='companyName']"
        self.next_button = "//a[@data-testid='pagination-page-next']"
        return

    def search(self, job_title):
        # opens indeed.com
        self.driver.get("https://www.indeed.com/")

        search_bar = self.wait.until(EC.presence_of_element_located((By.ID, 'text-input-what')))
        search_bar.send_keys(job_title)
        search_bar.send_keys(Keys.RETURN)

    def loop_results(self):
        # gets results from search page and scrolls through them
        # should get called whenever the next button is clicked

        driver = self.driver
        jobs_beacon = self.jobs_beacon
        jobs_beacon_a = self.jobs_beacon_a
        job_beacon_title = self.job_beacon_title
        job_beacon_company_name = self.job_beacon_company_name
        wait = self.wait

        # Get the list of jobs and companies on the current page
        jobs_on_page = driver.find_elements(By.XPATH, jobs_beacon + jobs_beacon_a)
        companies_on_page = driver.find_elements(By.XPATH, jobs_beacon + job_beacon_company_name)

        # Loop through each job on the page
        for index, job in enumerate(jobs_on_page):
            time.sleep(random.uniform(0, 2))
            if self.should_apply(job.text):
                driver.switch_to.window(driver.window_handles[0])
                job.click()
                print(job.text, end=": ")


            # Build XPath expression to locate the job based on its title
                xpath_expression = f'//div[@class="jobsearch-InfoHeaderContainer"]//span[contains(text(),"{job.text}")]'

                # Wait until the job's title text is present in the specified element (ID) on the page
                wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath_expression), job.text))

                initial_window_count = len(self.driver.window_handles)

                try:
                    # check if job can be applied through indeed's easy apply
                    apply_buttons = driver.find_elements(By.XPATH,
                                                         "//button[contains(@aria-label, 'Apply on company site') or @id='indeedApplyButton']")

                    if len(apply_buttons) > 0:
                        # Apply button(s) are present
                        if apply_buttons[0].get_attribute("id") == "indeedApplyButton":
                            # Handle the "Apply now" button case
                            self.driver.find_element(By.XPATH, "//button[@id='indeedApplyButton']").click()
                            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(initial_window_count + 1))
                            self.apply()
                        else:
                            pass
                            # Handle the "Apply on company site" button case
                            #print("Apply on company site button found")
                    else:
                        # No Apply buttons found
                        print("No Apply buttons found")

                    #button = self.driver.find_element((By.XPATH, "//button[@id='indeedApplyButton']"))
                    #button.click()
                    #WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(initial_window_count + 1))
                    #self.apply()

                    #driver.switch_to.window(driver.window_handles[-1])
                except:
                    #if a job cannot use easy apply
                    #print("rejected: " + job.text)
                    continue

            # wait.until(EC.presence_of_element_located(By.XPATH, "//*[text()='Add a resume for the employer']"))
            # driver.find_element_by_xpath("//div[@id='resume-display-buttonHeader']").click()
            # driver.find_element_by_xpath("//div[text()='Continue']").click()

            #apply = self.should_apply()

    def is_element_in_string(self, element_list, target_string):
        for element in element_list:
            if element in target_string:
                return True
        return False

    def should_apply(self, job_title):
        driver = self.driver

        #reads file into variable and cleans the file
        with open('prohibited_jobs', 'r') as file:
            menu_content = file.read()
        lines = menu_content.split('\n')
        lines = [line.strip() for line in lines]
        prohibited_job_titles = lines


        if self.job_is_allowed(prohibited_job_titles, job_title):
            return True
        else:
            return False

    def job_is_allowed(self, prohibited_job_titles, job_title):
        for prohibited_job in prohibited_job_titles:
            if prohibited_job.lower() in job_title.lower():
                return False
        return True

    def next(self):
        # clicks the next button on the results page
        # returns true if can click, otherwise returns false
        pass

    def organize_results(self):
        with open('tracks.txt', 'r') as file:
            lines = file.readlines()

        # Sort the lines alphabetically
        lines.sort()

        # Write the sorted lines back to the text file
        with open('tracks.txt', 'w') as file:
            file.writelines(lines)

    def record_job(self, job_name, company_name):
        with open('tracks.txt', 'a') as file:
            file.write(company_name + " || " + job_name + "\n")

        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='jobsearch-InfoHeaderContainer']//span[text()='{job_name}']")))

    def apply(self):
        print("Applied!")
        # applies to job
        # answers questions
        # pauses if doesn't know answer and prompts user
        # records questions and once prompt is exited, saves the answers
        # submits job aplication
        pass

    def job_in_database(self, job_title, company):
        # determines if job_title and company are recorded in database
        pass

    def get_driver(self):
        return self.driver

    def __del__(self):
        self.driver.quit()

# workflow
# go to indeed
# search feature
# get results
# loop through results
# land on job, determine if need to apply
# if apply:
# apply