#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support.ui import Select

import sys
import time
import csv

def login(driver, username, password):

    element = driver.find_element_by_id('username')

    element.send_keys(username)

    element = driver.find_element_by_id('password')

    element.send_keys(password)

    element.send_keys(Keys.RETURN)

    return element

def navigate_to_table(driver):
    config_id = "ALMA_MENU_TOP_NAV_configuration"

    config_element = driver.find_element_by_id(config_id).find_element_by_tag_name('button')

    config_element.click()

    url = "#CONF_MENU5"

    user_mgmt_element = driver.find_element_by_xpath('//a[@href="'+url+'"]')

    user_mgmt_element.click()

    mapping_table_div_id = "CONF_MENU5_2"

    mapping_table_element = driver.find_element_by_id(mapping_table_div_id).find_element_by_xpath(".//a[8]")

    mapping_table_element.click()



def enter_values(driver, row, file, success_counter, failure_counter):


    try:
        type_id = "pageBeannewRowrowsourceCode1_hiddenSelect"



        category_id = "pageBeannewRowrowtargetCode_hiddenSelect"

        code_element = driver.find_element_by_id(category_id)

        driver.find_element_by_id("pageBeannewRowrowtargetCode_hiddenSelect_button").click()

        time.sleep(.5)

        driver.find_element_by_link_text(row[0]).click()

        time.sleep(.5)


        select = Select(driver.find_element_by_id(type_id))

        time.sleep(.5)
        select.select_by_visible_text(row[1])




        driver.find_element_by_id("cbuttonaddRow").click()
        file.write(row[0] + "\t" + "Success\n")
        success_counter += 1
        time.sleep(.5)
    except:

        file.write(row[0] + "\t" + "Failure - enter manually\n")
        failure_counter += 1
        time.sleep(.5)

    return [success_counter, failure_counter]
