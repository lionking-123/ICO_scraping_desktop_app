import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def tradingview():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://www.tradingview.com/screener/'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(2)

    datas = {}
    trs = driver.find_elements_by_css_selector(
        "div.tv-screener__content-pane > table > tbody > tr")

    for tr in trs:

        data = {}
        try:
            tds = tr.find_elements_by_tag_name("td")
            sc_name = tr.find_element_by_css_selector(
                "a.tv-screener__symbol").text
            sc_mode = tr.find_element_by_css_selector(
                "span.tv-data-mode").text
            sc_description = tr.find_element_by_css_selector(
                "span.tv-screener__description").text

            data["Name"] = sc_name
            data["Mode"] = sc_mode
            data["Description"] = sc_description
        except:
            pass

        try:
            sc_last = tds[1].text
            sc_chg_per = tds[2].text
            sc_chg = tds[3].text
            sc_rating = tds[4].text
            sc_vol = tds[5].text
            sc_cap = tds[6].text
            sc_pe = tds[7].text
            sc_eps = tds[8].text
            sc_emp = tds[9].text
            sc_sector = tds[10].text

            data["LAST"] = sc_last
            data["CHG %"] = sc_chg_per
            data["CHG"] = sc_chg
            data["RATING"] = sc_rating
            data["VOL"] = sc_vol
            data["MKT CAP"] = sc_cap
            data["P/E"] = sc_pe
            data["EPS"] = sc_eps
            data["EMPLOYEES"] = sc_emp
            data["SECTOR"] = sc_sector
        except:
            pass

        datas[sc_name] = data

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/tradingview.csv")

    driver.close()
