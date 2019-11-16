#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

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

output_log = open("Output Log.txt", "w+")

output_log.write("Statistical Category\tStatus\n")

success_counter = 0

failure_counter = 0

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
        actions = ActionChains(driver)
        # actions.move_to_element(button_element)
        actions.move_to_element(button_element).click().perform();
        # button_element.click()
      except StaleElementReferenceException:
        continue # If StaleElement appears, try again
      break #


    values = enter_values(driver, row, output_log, success_counter, failure_counter)

    success_counter = values[0]
    failure_counter = values[1]
print("Counts: \n")
print("Values successfully entered:                   " + str(success_counter) + "\n")
print("Values that couldn't be entered (check log):   " + str(failure_counter) + "\n")

output_log.close()
table_file.close()
