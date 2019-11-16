#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

import csv
import sys
import time


from secrets import secrets

sys.path.append('scripts/')
from functions import *

from tkinter.filedialog import askopenfilename


print("\n\nChoose your tab-delimited text file of statistical categories and associated category types.\n\n")

time.sleep(1.5)
stat_category_table_file = askopenfilename(title = "Choose statistical category and type text file")

driver = webdriver.Chrome("c:/Users/hsteel01.TUFTS/chromedriver.exe")

driver.get("https://sandbox01-na.alma.exlibrisgroup.com/institution/01TUN_INST&auth=local")

element = login(driver, secrets.username, secrets.password)

navigate_to_table(driver)



table_file = open(stat_category_table_file, "r+")

table_reader = csv.reader(table_file, delimiter="\t")

time.sleep(.5)
for row in table_reader:
    time.sleep(.5)
    # driver.send_keys(Keys.PAGE_UP)

    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    button_element = driver.find_element_by_id("widgetId_Right_commappingTablesListlistheaderadd_row").find_element_by_tag_name('button')
    # time.sleep(1)


    while True:
      try:
        time.sleep(2)
        button_element.click()
      except StaleElementReferenceException:
        continue # If StaleElement appears, try again
      break #


    enter_values(driver, row)



table_file.close()
