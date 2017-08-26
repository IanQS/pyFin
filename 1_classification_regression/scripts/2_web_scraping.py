# coding: utf-8
import bs4 as bs
import pickle
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web

import requests


def save_SP500():
    src = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    resp = requests.get(src)
    soup = bs.BeautifulSoup(resp.text, "html5lib")
    table = soup.find("table", {"class": "wikitable sortable"})
    tickers = []
    for row in table.findAll("tr")[1:]:
        ticker = row.findAll("td")[0].text
        tickers.append(ticker)

    with open("S&P_500tickers.pkl", "wb") as f:
        pickle.dump(tickers, f)

    return tickers


def get_data_from_yahoo(reload_data=False):
    if reload_data:
        tickers = save_SP500()
    else:
        with open("S&P_500tickers.pkl", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists("stock_prices/"):
        os.makedirs("stock_prices/")

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2017, 7, 15)

    for ticker in tickers:
        ticker_fname = "stock_prices/{}_data.csv".format(ticker)
        if not os.path.exists(ticker_fname):
            try:
                df = web.get_data_yahoo(
                    ticker.replace('.', '-'),
                    start=start,
                    end=end
                )
                df.to_csv(ticker_fname)
            except:
                print("Failed to get data for ticker: {0}".format(ticker))
        else:
            pass
            # print("Found data file for {0}".format(ticker))


get_data_from_yahoo()


def compile_data(ignore, csv_folder="stock_prices/",
                 ticker_names="S&P_500tickers.pkl"):

    with open(ticker_names, "rb") as f:
        tickers = pickle.load(f)

    compiled_df = pd.DataFrame()

    for i, ticker in enumerate(tickers):

        # Sometimes when scraping we can't get all the data. Can either
        # manually scrape it later, or ignore it like we're doing now
        if ticker in ignore:
            continue

        df = pd.read_csv(csv_folder + "{0}_data.csv".format(ticker))

        # Index all the data via the dates
        df.set_index("Date", inplace=True)
        df.rename(columns={"Adj Close": ticker}, inplace=True)
        df.drop(["Open", "High", "Low", "Close", "Volume"], 1, inplace=True)

        if compiled_df.empty:
            compiled_df = df
        else:
            compiled_df = compiled_df.join(df, how="outer")

        if i % 50 == 0:
            print(i)
#     print(compiled_df.head())

    compiled_df.to_csv("S&P500_joined_adj-close.csv")


ignore = [
    "HLT", "LVLT", "STI", "WU", "WRK", "WY", "WHR", "WFM", "WMB", "WLTW",
    "WYN", "WYNN", "XEL", "XRX", "XLNX", "XL", "XYL", "YUM", "ZBH", "ZION",
    "ZTS"
]
compile_data(ignore)
