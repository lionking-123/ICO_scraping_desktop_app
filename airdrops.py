import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def airdrops():
    src = 'https://airdrops.io/hot/'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    driver = webdriver.Chrome("./UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(1)

    for i in range(10):
        try:
            showBtn = driver.find_element_by_css_selector(
                "div.showmore > span")
            showBtn.click()
            time.sleep(1)
        except:
            pass

    urls = []
    divs = driver.find_elements_by_css_selector("article.airdrop-hover > div")

    for div in divs:
        url = div.get_attribute("onclick")
        idx = str(url).index("'")
        urls.append(url[idx + 1:-1])

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
                name = driver.find_element_by_css_selector(
                    "h1.entry-title").text
                data["Name"] = name

                lis = driver.find_elements_by_css_selector(
                    "div.airdrop-logo-thumbnail > div.airdrop-info > ul > li")
                for li in lis:
                    li_text = li.text
                    if("starts" in li_text):
                        data["Start Date"] = str(li_text).replace(
                            "Airdrop starts ", "")
                    elif("ends" in li_text):
                        data["End Date"] = str(li_text).replace(
                            "Airdrop ends ", "")
                    elif("Link" in li_text):
                        ahref = driver.find_element_by_css_selector(
                            "div.airdrop-logo-thumbnail > div.airdrop-info > ul > li > a").get_attribute("href")
                        data["Airdrop Link"] = ahref
                    elif("value" in li_text):
                        data["Total Value"] = str(
                            li_text).replace("Total value: ", "")
                    elif("Platform" in li_text):
                        data["Platform"] = str(
                            li_text).replace("Platform: ", "")
            except:
                pass

            try:
                description = driver.find_element_by_css_selector(
                    "span.drop-features > p").text + "\n"
                description += driver.find_element_by_css_selector(
                    "div.aidrop-info-wrapper > div:nth-child(2) > p").text
                data["Description"] = description

                guide = driver.find_elements_by_css_selector(
                    "div.airdrop-guide > ol")[0].text
                data["Step-by-Step Guide"] = guide
            except:
                pass

            try:
                data["Estimated Value"] = driver.find_element_by_css_selector(
                    "div.aidrop-grid-wrapper > div:nth-child(1) > p").text
                data["Tokens per Claim"] = driver.find_element_by_css_selector(
                    "div.aidrop-grid-wrapper > div:nth-child(2) > p").text
                data["Max. Participants"] = driver.find_element_by_css_selector(
                    "div.aidrop-grid-wrapper > div:nth-child(3) > p").text
            except:
                pass

            try:
                lis = driver.find_elements_by_css_selector(
                    "div.airdrop-list > ul > li")
                for li in lis:
                    li_text = li.text
                    idx = str(li_text).index(":")
                    try:
                        atag = li.find_element_by_tag_name("a")
                        data[li_text[:idx]] = atag.get_attribute("href")
                    except:
                        data[li_text[:idx]] = li_text[idx + 2:]
            except:
                pass

            datas[name] = data

            driver.close()
        except:
            pass

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/airdrops.csv")
