import gc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def cryptorank():
    src = 'https://cryptorank.io/upcoming-ico'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option, desired_capabilities=capa)
    wait = WebDriverWait(driver, 9)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'table.table > tbody > tr > td:nth-child(1) > div > a')))
    driver.execute_script("window.stop();")

    urls = []
    atags = driver.find_elements_by_css_selector(
        "table.table > tbody > tr > td:nth-child(1) > div > a")
    for atag in atags:
        tmp = atag.get_attribute("href")
        if("undefined" not in tmp):
            urls.append(tmp)

    driver.quit()
    datas = {}

    for url in urls:
        try:
            driver = webdriver.Chrome(
                "./UI/chromedriver", options=option, desired_capabilities=capa)
            wait = WebDriverWait(driver, 9)
            driver.get(url)
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'h2[class*="CoinMainHeader"]')))
            driver.execute_script("window.stop();")

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
                data["Goal"] = driver.find_elements_by_css_selector(
                    "div[class*='IcoInfoValue']")[1].text
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
                    if(soc_title == "Website"):
                        soc_link = str(soc_link).replace(
                            "/?utm_source=cryptorank", "")

                    data[soc_title] = soc_link
            except:
                pass

            try:
                divs = driver.find_elements_by_css_selector(
                    "div[class*='TokenEconomicsBlock'] > div[class*='columns__Column'] > div > div")
                data["Total Raised"] = divs[0].text

                for i in range(1, len(divs)):
                    cont_text = divs[i].text
                    id = str(cont_text).index(":")
                    if("Market" in cont_text):
                        data["Market cap"] = cont_text[id + 2:]
                    elif("FDMC" in cont_text):
                        data["FDMC"] = cont_text[id + 2:]
                    else:
                        data["Circulating Supply"] = cont_text[id + 2:]

            except:
                pass

            try:
                divs = driver.find_elements_by_css_selector(
                    "div[class*='SupplyRow']")
                for div in divs:
                    title = div.find_elements_by_tag_name("div")[0].text
                    value = div.find_elements_by_tag_name("div")[1].text
                    data[title] = value
            except:
                pass

            datas[ico_name] = data

            driver.quit()
        except:
            pass

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/cryptorank.csv")

    gc.collect()
