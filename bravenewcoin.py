import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def bravenewcoin():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://bravenewcoin.com/events'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(3)

    while(True):
        try:
            btn = driver.find_element_by_css_selector("button.ladda-button")
            btn.click()
            time.sleep(2)
        except:
            break

    datas = {}
    divs = driver.find_elements_by_css_selector("div.event-item.col-12")

    for div in divs:
        data = {}
        try:
            event_date = div.find_element_by_css_selector(
                "div.event-date > div").text
            event_date = str(event_date).replace("\n", " ")
            data["Event Date"] = event_date
        except:
            pass

        try:
            event_name = div.find_element_by_css_selector(
                "div.event-name > a").text
            data["Event Name"] = event_name
        except:
            pass

        try:
            event_type = div.find_element_by_css_selector(
                "div.event-type > span").text
            data["Event Type"] = event_type
        except:
            pass

        try:
            event_location = div.find_element_by_css_selector(
                "div.event-location").text
            data["Event Location"] = event_location
        except:
            pass

        datas[event_name] = data

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/bravenewcoin.csv")

    driver.close()
