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



def enter_values(driver, row):


    #
    # category_id = "pageBeannewRowrowtargetCode_hiddenSelect"
    #
    # type_id = "pageBeannewRowrowsourceCode1_hiddenSelect"


    type_id = "pageBeannewRowrowsourceCode1_hiddenSelect"



    category_id = "pageBeannewRowrowtargetCode_hiddenSelect"

    # driver.find_element_by_id(type_id).send_keys(" ")
    #
    # type_element = driver.find_element_by_id(type_id)
    #
    #
    # # driver.find_element_by_id("pageBeannewRowrowsourceCode1_hiddenSelect_button").click()
    #
    # # type_element.click()
    # # # type_element.find_element_by_link_text(row[1]).click()
    # driver.find_element_by_link_text(row[1]).click()

    # code_element = Select(driver.find_element_by_id(category_id).find_element_by_xpath(".//option[text() = '" + row[0] + "']"))
    # code_element = driver.find_element_by_id(category_id)
    # code_element.click()
    # code_element.find_element_by_link_text(row[0]).click()
    code_element = driver.find_element_by_id(category_id)

    driver.find_element_by_id("pageBeannewRowrowtargetCode_hiddenSelect_button").click()

    time.sleep(1)

    driver.find_element_by_link_text(row[0]).click()

    time.sleep(1)
    #
    # type_element = driver.find_element_by_id(type_id)
    #
    # time.sleep(1)
    # # driver.execute_script("window.scrollTo(0, 0)")
    #
    # #
    # table_element = driver.find_element_by_id("link_action_widget_com.mappingTablesList.list.header.add_row")
    #
    # time.sleep(.5)
    # table_element.find_element_by_xpath('//button[@id="pageBeannewRowrowsourceCode1_hiddenSelect_button"]').click()
    #
    # time.sleep(1)
    #
    # driver.find_element_by_link_text(row[1]).click()


    # while True:
    #   try:
    if driver.find_element_by_id("cbuttonaddRow").is_displayed():
        driver.find_element_by_id("cbuttonaddRow").click()

      # except StaleElementReferenceException:
      #   continue # If StaleElement appears, try again
      # break #

    # time.sleep(2)

    # driver.find_element_by_id("link_action_widget_com.mappingTablesList.list.header.add_row").find_elements_by_tag_name('li')[0].find_elements_by_tag_name('button')[0].click()

    # code_element = Select(driver.find_element_by_id(category_id))
    # action = ActionChains(driver)
    #
    # action.move_to_element(code_element).click().perform()
    # code_element.send_keys(Keys.PAGE_DOWN)
    # code_element.select_by_value(row[0])
    #
    # type_element = Select(driver.find_element_by_id(type_id))
    # type_element.select_by_value(row[1])


    # codeElement.se
    # # driver.execute_script("arguments[0].click()", code_element)
    #
    # type_element = driver.find_element_by_id(type_id).find_element_by_xpath(".//option[text() = '" + row[1] + "']")
    # driver.execute_script("arguments[0].click()", type_element)

    # driver.find_element_by_id(category_id).send_keys(row[0])
    #
    #
    # driver.find_element_by_id(type_id).send_keys(" ")
    # driver.find_element_by_id(type_id).send_keys(row[1])



    # close_id = "link_action_widget_com.mappingTablesList.list.header.add_row"
    #
    # time.sleep(2)
    # close_button = driver.find_element_by_id(close_id).find_element_by_tag_name('li')[0].find_element_by_tag_name('button')[0];
    # close_button.click()
