class database:
    def job_in_database(self, job_title, company):
        # determines if job_title and company are recorded in database
        pass

    def record_job(self, job_name, company_name):
        with open('tracks.txt', 'a') as file:
            file.write(company_name + " || " + job_name + "\n")

        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='jobsearch-InfoHeaderContainer']//span[text()='{job_name}']")))

    def organize_results(self):
        with open('tracks.txt', 'r') as file:
            lines = file.readlines()

        # Sort the lines alphabetically
        lines.sort()

        # Write the sorted lines back to the text file
        with open('tracks.txt', 'w') as file:
            file.writelines(lines)
