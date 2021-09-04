import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def airdropalert():
    src = 'https://airdropalert.com/new-airdrops?page='
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    driver = webdriver.Chrome("./UI/chromedriver", options=option)

    urls = []
    for i in range(1, 15):
        driver.get(src + str(i))
        time.sleep(1)

        atags = driver.find_elements_by_css_selector("a.card-link-overlay")

        for atag in atags:
            urls.append(atag.get_attribute("href"))

    driver.close()

    datas = {}

    count = 1
    for url in urls:
        if(count > 3):
            break
        count = count + 1

        driver = webdriver.Chrome("./UI/chromedriver", options=option)
        driver.get(url)
        time.sleep(1)
        data = {}

        try:
            name = driver.find_element_by_css_selector(
                "h1.airdrop__title").text
            name = str(name).replace(" Airdrop", "")
            idx = str(name).index("(")

            data["Name"] = name[:idx - 1]

            atags = driver.find_elements_by_css_selector(
                "div.airdrop__social > a")
            for atag in atags:
                if("Facebook" in atag.get_attribute("title")):
                    data["Facebook link"] = atag.get_attribute("href")
                elif("Reddit" in atag.get_attribute("title")):
                    data["Reddit link"] = atag.get_attribute("href")
                elif("Twitter" in atag.get_attribute("title")):
                    data["Twitter link"] = atag.get_attribute("href")
                elif("Telegram" in atag.get_attribute("title")):
                    data["Telegram link"] = atag.get_attribute("href")
                elif("Medium" in atag.get_attribute("title")):
                    data["Medium link"] = atag.get_attribute("href")
                elif("Discord" in atag.get_attribute("title")):
                    data["Discord link"] = atag.get_attribute("href")
                elif("Youtube" in atag.get_attribute("title")):
                    data["Youtube link"] = atag.get_attribute("href")
                elif("information" in atag.get_attribute("title")):
                    data["Website"] = atag.get_attribute("href")
                elif("directly" in atag.get_attribute("title")):
                    data["Directly link"] = atag.get_attribute("href")
                else:
                    data["Whitepaper"] = atag.get_attribute("href")
        except:
            pass

        try:
            description = driver.find_element_by_css_selector(
                "div.airdrop__content > p:nth-child(1)").text
            data["Description"] = description
        except:
            pass

        try:
            divs = driver.find_elements_by_css_selector(
                "div.airdrop-widget > div")
            for div in divs:
                title = div.find_element_by_tag_name("strong").text
                cont = str(div.text).replace(title, "").strip()
                data[title] = cont
        except:
            pass

        try:
            guide = driver.find_element_by_css_selector(
                "div.page-description > ol").text
            data["Step-by-Step Guide"] = guide

            claimBtn = driver.find_element_by_css_selector(
                "div.airdrop-flex-buttons > div > button").get_attribute("data-url")
            data["Claim Airdrop"] = claimBtn

            nextBtn = driver.find_element_by_css_selector(
                "div.airdrop-flex-buttons > div:nth-child(3) > a").get_attribute("href")
            data["Next Airdrop"] = nextBtn
        except:
            pass

        try:
            est = driver.find_element_by_css_selector("div.est-temp").text
            data["Estimated value"] = str(est).replace(
                "Estimated value", "").strip()
        except:
            pass

        datas[name] = data

        driver.close()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/airdropalert.csv")
