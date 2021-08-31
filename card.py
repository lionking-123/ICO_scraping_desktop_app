import re
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.common.exceptions import NoSuchElementException

def card_info(flg) :
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://www.getcreditcardnumbers.com/'
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(path+"/UI/chromedriver",options = option)
    driver.get(src)
    time.sleep(1)
    
    option_flag = flg #'AE' master card:MC, Aexpress: AE, visa:V, discover: D
    driver.find_element_by_xpath("//select[@name='card_type']/option[@value='" + str(option_flag)+"']").click()
    time.sleep(1)
    div = driver.find_element_by_class_name('prettyprint.linenums')
    form = div.text
    cardnumber = re.findall(r'\d+',form)[0]

    return cardnumber
