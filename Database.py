class Database:

    def __init__(self):
        pass
    def job_in_database(self, job_title, company):
        # determines if job_title and company are recorded in database
        pass

    def record_job(self, job_name, company_name):
        with open('database.txt', 'a') as file:
            file.write(company_name + " || " + job_name + "\n")


    def organize_results(self):
        with open('tracks.txt', 'r') as file:
            lines = file.readlines()

        # Sort the lines alphabetically
        lines.sort()

        # Write the sorted lines back to the text file
        with open('tracks.txt', 'w') as file:
            file.writelines(lines)

    def read_data(self, job_title="", company=""):
        """"
        if (job in database)
            TITLE:
        COMPANY:
        APPLIED:

        else:
        Job not in database
        """