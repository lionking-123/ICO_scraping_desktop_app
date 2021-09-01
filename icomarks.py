import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


def icomarks():
    path = os.path.dirname(os.path.abspath(__file__))
    src = 'https://icomarks.com/icos'
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(path+"/UI/chromedriver", options=option)
    driver.get(src)
    time.sleep(1)

    urls = []
    atags = driver.find_elements_by_css_selector("a.icoListItem__title")
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
                "h1[itemprop = 'name']").text
            ico_active = driver.find_element_by_css_selector(
                "div.ico-active").text
            ico_description = driver.find_element_by_css_selector(
                "div.company-description").text
            ico_comment_views = driver.find_element_by_css_selector(
                "div.comment-views").text
            ico_active = str(ico_active).replace(ico_comment_views, "")

            data["ICO Name"] = ico_name
            data["ICO Active"] = ico_active
            data["ICO Comment Views"] = ico_comment_views
            data["ICO Description"] = ico_description
        except:
            pass

        try:
            total_score = driver.find_element_by_css_selector(
                "div.ico-rating-overall").text
            ico_profile = str.split(str(driver.find_elements_by_css_selector(
                "div.ico-rating__circle")[0].text), "\n")[0]
            ico_profile = ico_profile + (str(driver.find_elements_by_css_selector(
                "div.ico-rating__title > p")[0].text))
            social_activity = str.split(str(driver.find_elements_by_css_selector(
                "div.ico-rating__circle")[1].text), "\n")[0]
            social_activity = social_activity + (str(driver.find_elements_by_css_selector(
                "div.ico-rating__title > p")[1].text))
            team_proof = str.split(str(driver.find_elements_by_css_selector(
                "div.ico-rating__circle")[2].text), "\n")[0]
            team_proof = team_proof + (str(driver.find_elements_by_css_selector(
                "div.ico-rating__title > p")[2].text))

            data["Total Score"] = total_score
            data["ICO Profile"] = ico_profile
            data["Social Activity"] = social_activity
            data["Team Proof"] = team_proof

        except:
            pass

        try:
            divs = driver.find_elements_by_css_selector(
                "div.icoinfo-block__item")
            for div in divs:
                span_text = div.find_element_by_tag_name("span").text
                span_text = str(span_text).replace(":", "")
                if(("Links" in span_text) or (span_text == "")):
                    soc_link = div.find_element_by_tag_name(
                        "a").get_attribute("href")
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
                elif(("Website" in span_text) or ("White paper" in span_text) or ("MVP" in span_text)):
                    link = div.find_element_by_tag_name(
                        "a").get_attribute("href")
                    data[span_text] = link
                else:
                    li_text = str(div.text).replace(span_text, "")[2:]
                    data[span_text] = li_text
        except:
            pass

        datas[ico_name] = data

        driver.close()

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/icomarks.csv")
