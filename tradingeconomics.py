import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def tradingeconomics():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://tradingeconomics.com/'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(3)

    while(True):
        try:
            btn = driver.find_element_by_css_selector("button.btn-default")
            btn.click()
            time.sleep(2)
        except:
            break

    datas = {}
    trs = driver.find_elements_by_css_selector(
        "table[id*='ContentPlaceHolder'] > tbody > tr")

    for tr in trs:
        data = {}
        try:
            tds = tr.find_elements_by_tag_name("td")
            cntry = tds[0].text
            con1 = tds[1].text
            con2 = tds[2].text
            con3 = tds[3].text
            con4 = tds[4].text
            con5 = tds[5].text
            con6 = tds[6].text
            con7 = tds[7].text
            con8 = tds[8].text
            con9 = tds[9].text
            con10 = tds[10].text

            data["Country"] = cntry
            data["GDP"] = con1
            data["GDP YoY"] = con2
            data["GDP QoQ"] = con3
            data["Interest rate"] = con4
            data["Inflation rate"] = con5
            data["Jobless rate"] = con6
            data["Gov. Budget"] = con7
            data["Debt/GDP"] = con8
            data["Current Account"] = con9
            data["Population"] = con10

            datas[cntry] = data
        except:
            pass

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/tradingeconomics.csv")

    driver.close()
