# https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
# https://pypi.python.org/pypi/selenium
# https://www.selenium.dev/downloads/  downlod  drivers
# https://sites.google.com/a/chromium.org/chromedriver/downloads  driver version must match installed chrome version
# See discussions of Python Splinter Vs Selenium
# scrapy is faster than Selenium but harder to use
# Documentation: https://selenium-python.readthedocs.io/locating-elements.html
# Alternative libraries for Web Scraping: Splinter, requests_html


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os



# Take Screenshot  driver.save_screenshot(f".\images\snapshot.png")

def tab(df):
    print(tabulate(df, headers='keys', tablefmt='rst'))





def example_explicit_wait():

    # Create a new chromedriver instance
    driver = webdriver.Chrome()

    # Go to www.google.com
    driver.get("https://www.google.com")

    try:
        # Wait as long as required, or maximum of 5 sec for element to appear
        # If successful, retrieves the element
        element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME, "q")))

        # Type "selenium"
        element.send_keys("selenium")

        #Type Enter
        element.send_keys(Keys.ENTER)

    except TimeoutException:
        print("Failed to load search bar at www.google.com")
    finally:
        driver.quit()



def example_implicit_wait():
    # launch url
    url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

    # download web driver from here https://www.selenium.dev/downloads/
    # create a new session
    driver = webdriver.Chrome()  # chromedriver must be in current drive of .py file or on PATH
    driver.implicitly_wait(30)   # Any 'find element' command will implicitly wait up to 30 secs to find it before
                                 # Issuing an Exception. This applies until driver.quit()



    driver.get(url)



    # Find the fields and enter credentials
    # username = driver.find_element_by_id("username")
    # password = driver.find_element_by_id("pass")
    # username.send_keys("vhallen@tscinsurance.com")
    # password.send_keys("tsc2017!")
    # driver.find_element_by_tag_name('button').submit()

    # username.clear()  # this would empty the field


    # obj = driver.find_element_by_class_name('xxx')
    # obj =  driver.find_element_by_id('xxx')
    # obj =  driver.find_element_by_tag_name('button')
    # 'find_element', \
    # 'find_element_by_class_name', \
    # 'find_element_by_css_selector', \
    # 'find_element_by_id', \
    # 'find_element_by_link_text', \
    # 'find_element_by_name', \
    # 'find_element_by_partial_link_text', \
    # 'find_element_by_tag_name', \
    # 'find_element_by_xpath',
    #

    # After opening the url above, Selenium clicks the specific agency link
    python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')  # FHSU
    python_button.click()  # click fhsu link

    # Selenium hands the page source to Beautiful Soup
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')

    datalist = []  # empty list
    x = 0  # counter

    # Beautiful Soup finds all Job Title links on the agency page and the loop begins
    for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
        # Selenium visits each Job Title page
        python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
        python_button.click()  # click link

        # Selenium hands of the source of the specific job page to Beautiful Soup
        soup_level2 = BeautifulSoup(driver.page_source, 'lxml')

        # Beautiful Soup grabs the HTML table on the page
        table = soup_level2.find_all('table')[0]

        # Giving the HTML table to pandas to put in a dataframe object
        df = pd.read_html(str(table), header=0)

        # Store the dataframe in a list
        datalist.append(df[0])

        # Ask Selenium to click the back button
        driver.execute_script("window.history.go(-1)")

        # increment the counter variable before starting the loop over
        x += 1

        # end loop block
        if x == 3:
            break

    # loop has completed

    # end the Selenium browser session
    driver.quit()

    # combine all pandas dataframes in the list into one big dataframe
    result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))], ignore_index=True)


    # pretty print to CLI with tabulate
    # converts to an ascii table
    print(tabulate(result, headers=["Employee Name", "Job Title", "Overtime Pay", "Total Gross Pay"], tablefmt='psql'))




# ======================================================================================================================
if __name__ == '__main__':
    example_explicit_wait()
    #example_implicit_wait()
