from selenium.webdriver.common.keys import Keys
from Indeed import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logIn import *

indeed = indeed()

driver = indeed.get_driver()

indeed.search("Software QA")

indeed.loop_results()

indeed.organize_results()

print("done")




