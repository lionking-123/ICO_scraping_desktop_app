import gc
import requests
import pandas as pd


def tradingview():
    req = requests.post("https://scanner.tradingview.com/america/scan", json={"filter": [{"left": "name", "operation": "nempty"}], "options": {"lang": "en"}, "symbols": {"query": {
                        "types": []}, "tickers": []}, "columns": ["name", "description", "number_of_employees", "sector", "subtype"], "sort": {"sortBy": "name", "sortOrder": "desc"}, "range": [0, 10000]})

    res = req.json()
    tot = res["totalCount"]

    datas = {}

    for i in range(10000):
        data = {}
        data["Ticker"] = res["data"][i]["d"][0]
        data["Name"] = res["data"][i]["d"][1]
        data["EMPLYEES"] = res["data"][i]["d"][2]
        data["SECTOR"] = res["data"][i]["d"][3]
        data["Stock Type"] = res["data"][i]["d"][4]

        datas[res["data"][i]["d"][0]] = data

    df = pd.DataFrame(data=datas).T
    df.to_csv("./results/tradingview.csv")

    gc.collect()
