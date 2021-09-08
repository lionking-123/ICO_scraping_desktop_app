import gc
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def icodrops():
    src = 'https://icodrops.com/'
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(
        "./UI/chromedriver", options=option, desired_capabilities=capa)
    wait = WebDriverWait(driver, 9)

    driver.get(src)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'a#n_color')))
    driver.execute_script("window.stop();")

    urls = []
    atags = driver.find_elements_by_css_selector("a#n_color")
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
                (By.CSS_SELECTOR, 'div.ico-main-info > h3')))
            driver.execute_script("window.stop();")

            data = {}
            try:
                ico_name = driver.find_element_by_css_selector(
                    "div.ico-main-info > h3").text
                ico_category = str.split(str(driver.find_element_by_css_selector(
                    "span.ico-category-name").text), "\n")[0]
                ico_category = ico_category[1:-1]
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
                data["Money Goal"] = money_goal[1:]
            except:
                pass

            try:
                goal = driver.find_element_by_css_selector(
                    "div.fund-goal > div.goal").text
                goal = str(goal).replace("OF\n$", "")
                id = str(goal).index("(")
                data["Goal"] = goal[:id]
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

            try:
                links = driver.find_elements_by_css_selector(
                    "div.soc_links > a")
                for link in links:
                    soc_link = link.get_attribute("href")
                    if("facebook" in soc_link):
                        data["Facebook link"] = soc_link
                    elif("reddit" in soc_link):
                        data["Reddit link"] = soc_link
                    elif("twitter" in soc_link):
                        data["Twitter link"] = soc_link
                    elif("t.me" in soc_link):
                        data["Telegram link"] = soc_link
                    elif("medium" in soc_link):
                        data["Medium link"] = soc_link
                    elif("discord" in soc_link):
                        data["Discord link"] = soc_link
                    else:
                        data["Youtube link"] = soc_link
            except:
                pass

            try:
                token_sale = driver.find_elements_by_css_selector(
                    "div.title-h4 > h4")[0].text
                token_sale = str(token_sale).replace("TOKEN Sale: ", "")
                id = str(token_sale).index("-")
                data["Start_date"] = token_sale[:id-1]
                data["End_date"] = token_sale[id+2:]
            except:
                pass

            try:
                lis = driver.find_elements_by_css_selector(
                    "div.list > div > li")
                for li in lis:
                    li_text = li.text
                    span_text = li.find_element_by_tag_name("span").text
                    li_text = str(li_text).replace(span_text, "")[1:]
                    span_text = str(span_text).replace(":", "")
                    if(span_text == "ICO Token Price"):
                        id = str(li_text).index("=")
                        data["ICO Price"] = li_text[id + 2:-4]
                    else:
                        data[span_text] = li_text
            except:
                pass

            try:
                atags = driver.find_elements_by_css_selector(
                    "div.list-thin > div >li > a")
                id = 1
                for atag in atags:
                    add_link = atag.text
                    data["Addional Link{}".format(id)] = str(
                        add_link + " # " + atag.get_attribute("href"))
                    id = id + 1
            except:
                pass

            datas[ico_name] = data

            driver.quit()
        except:
            pass

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/icodrops.csv")

    gc.collect()
