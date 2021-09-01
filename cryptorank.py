import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def cryptorank():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://cryptorank.io/upcoming-ico'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(1)

    urls = []
    atags = driver.find_elements_by_css_selector(
        "table.table > tbody > tr > td:nth-child(1) > div > a")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    driver.close()
    datas = {}

    count = 1
    for url in urls:
        if(count > 3):
            break
        count = count + 1
        driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
        driver.get(url)
        time.sleep(1)
        data = {}
        try:
            ico_name = driver.find_element_by_css_selector(
                "h2[class*='CoinMainHeader']").text
            id1 = str(ico_name).index("[")
            id2 = str(ico_name).index("]")
            ico_secondary = ico_name[id1 + 1:id2]
            ico_name = ico_name[:id1 - 1]

            ico_description = driver.find_element_by_css_selector(
                "div[class*='CoinSubheader'] > p").text

            data["ICO Name"] = ico_name
            data["ICO Secondary"] = ico_secondary
            data["ICO Description"] = ico_description
        except:
            pass

        try:
            data["TokenSale"] = driver.find_elements_by_css_selector(
                "div[class*='IcoInfoValue']")[0].text
            data["FundraisingGoal"] = driver.find_elements_by_css_selector(
                "div[class*='IcoInfoValue']")[1].text
            data["Interest Rate"] = driver.find_elements_by_css_selector(
                "div[class*='IcoInfoValue']")[2].text
        except:
            pass

        try:
            tokens = driver.find_elements_by_css_selector(
                "div[class*='ContainerCoinLabel'] > a")
            token_text = ""
            for token in tokens:
                token_text += (token.text + ", ")

            data["TOKEN"] = token_text[:-2]
        except:
            pass

        try:
            links = driver.find_elements_by_css_selector(
                "div[class*='CoinIconLinksBlock'] > a")
            for link in links:
                soc_link = link.get_attribute("href")
                soc_title = link.get_attribute("title")

                data[soc_title] = soc_link
        except:
            pass

        try:
            divs = driver.find_elements_by_css_selector(
                "div[class*='TokenEconomicsBlock'] > div[class*='columns__Column'] > div > div")
            data["Total Raised"] = divs[0].text

            initial_values = ""
            for i in range(1, len(divs)):
                initial_values += (divs[i].text + "\n")

            data["Initial Values"] = initial_values[:-1]
        except:
            pass

        try:
            divs = driver.find_elements_by_css_selector(
                "div[class*='SupplyRow']")
            token_alloc = ""
            for div in divs:
                title = div.find_elements_by_tag_name("div")[0].text
                value = div.find_elements_by_tag_name("div")[1].text
                token_alloc += (title + value + "\n")

            data["Token Allocation"] = token_alloc[:-1]
        except:
            pass

        datas[ico_name] = data

        driver.close()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/cryptorank.csv")
