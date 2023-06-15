from selenium.webdriver.common.keys import Keys
from Indeed import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from logIn import *

indeed = indeed()

indeed.search("Software QA")

indeed.loop_results()

print("done")




