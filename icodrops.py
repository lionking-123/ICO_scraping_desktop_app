import re
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def icodrops():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://icodrops.com/'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(1)

    urls = []
    atags = driver.find_elements_by_css_selector("a#n_color")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    driver.close()
    datas = {}

    for url in urls:
        driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
        driver.get(url)
        time.sleep(1)
        data = {}
        try:
            ico_name = driver.find_element_by_css_selector(
                "div.ico-main-info > h3").text
            ico_category = str.split(str(driver.find_element_by_css_selector(
                "span.ico-category-name").text), "\n")[0]
            ico_description = driver.find_element_by_css_selector(
                "div.ico-description").text
            ico_important = driver.find_element_by_css_selector(
                "div.important-note").text
            ico_important = str(ico_important).replace("Important: ", "")

            data["ICO Name"] = ico_name
            data["ICO Category Name"] = ico_category
            data["ICO Description"] = ico_description
            data["ICO Important"] = ico_important
        except:
            pass

        try:
            money_goal = driver.find_element_by_css_selector(
                "div.fund-goal > div.money-goal").text
            data["Money Goal"] = money_goal
        except:
            pass

        try:
            goal = driver.find_element_by_css_selector(
                "div.fund-goal > div.goal").text
            data["Goal"] = goal
        except:
            pass

        try:
            website = driver.find_elements_by_css_selector(
                "div.ico-right-col > a")[0].get_attribute("href")
            data["Website"] = website
        except:
            pass

        try:
            whitepaper = driver.find_elements_by_css_selector(
                "div.ico-right-col > a")[1].get_attribute("href")
            data["Whitepaper"] = whitepaper
        except:
            pass

        datas[ico_name] = data

        driver.close()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/icodrops.csv")
