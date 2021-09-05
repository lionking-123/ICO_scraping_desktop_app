import os
import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def coincodex():
    src = 'https://coincodex.com/sto-list/'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    driver = webdriver.Chrome("./UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(1)

    urls = []
    atags = driver.find_elements_by_css_selector("tr > td:nth-child(1) > a")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    driver.close()
    datas = {}

    count = 1
    for url in urls:
        try:
            if(count > 3):
                break
            count = count + 1
            driver = webdriver.Chrome("./UI/chromedriver", options=option)
            driver.get(url)
            time.sleep(1)
            data = {}
            try:
                ico_name = driver.find_element_by_css_selector(
                    "header.main-title > h1").text
                id = str(ico_name).index("(")
                ico_symbol = ico_name[id:]
                ico_name = ico_name[:id]

                ico_description = driver.find_element_by_css_selector(
                    "div.about-box-text > p").text

                data["ICO Name"] = ico_name
                data["ICO Symbol"] = ico_symbol
                data["ICO Description"] = ico_description
            except:
                pass

            try:
                links = driver.find_elements_by_css_selector(
                    "div.about-box-links > ul > li > a")
                for link in links:
                    soc_link = link.get_attribute("href")
                    soc_text = link.text
                    data[str.capitalize(soc_text)] = soc_link
            except:
                pass

            try:
                sto_dates = driver.find_elements_by_css_selector(
                    "div.ico-timeline-value")[1].text
                data["STO Dates"] = sto_dates
                data["Current Stage"] = "STO"
            except:
                pass

            try:
                trs = driver.find_elements_by_css_selector("tr.ico-data-entry")
                for i in range(4, 8):
                    cls_text = trs[i].find_element_by_css_selector(
                        "th > span").text
                    val_text = trs[i].find_element_by_css_selector(
                        "td > span").text
                    data[cls_text] = val_text
            except:
                pass

            try:
                unkown = driver.find_elements_by_css_selector(
                    "div.token-distribution > ul > li > span")[0].text
                investors = driver.find_elements_by_css_selector(
                    "div.token-distribution > ul > li > span")[1].text
                data["Token Distribution"] = "UNKOWN " + \
                    unkown + "/" + "INVESTORS " + investors
            except:
                pass

            datas[ico_name] = data

            driver.close()
        except:
            pass

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/cioncodex.csv")

    gc.collect()
