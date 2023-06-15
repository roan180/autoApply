class Database:

    def __init__(self):
        pass
    def job_in_database(self, job_title, company):
        with open('database.txt') as f:
            if (job_title + " || " + company) in f.read():
                return True
        return False

    def record_job(self, job_name, company_name):
        with open('database.txt', 'a') as file:
            file.write(job_name + " || " + company_name + "\n")

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