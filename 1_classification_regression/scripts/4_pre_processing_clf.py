# coding: utf-8
# Handle the plotting
import matplotlib.pyplot as plt
from matplotlib import style
style.use("seaborn-deep")

# For data processing
import pandas as pd
import numpy as np

# For getting the data

from collections import Counter


def process_data_for_labels(src, ticker, num_days):
    df = pd.read_csv(src, index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, num_days + 1):
        col_name = '{}_{}d'.format(ticker, i)
        df[col_name] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df


def classify(*args):
    """
    return 0,1,2 so that we can construct matrices for our "labels" to allow us
    to use categorical cross entropy function
    """
    cols = [c for c in args]
    tol = 0.02
    for col in cols:
        if col > tol:
            return 0
        if col < -tol:
            return 2
    return 1


def extract_featuresets_clf(src, ticker, num_days, plot=False):
    tickers, df = process_data_for_labels(src, ticker, num_days)
    col_name = '{}_target'.format(ticker)

    df[col_name] = list(
        map(
            classify,
            *[df['{}_{}d'.format(ticker, i)] for i in range(1, num_days + 1)]
        )
    )

    # Just getting an idea of the underlying y distribution
    vals = df[col_name].values.tolist()
    str_vals = [str(i) for i in vals]
    if plot:
        plt.hist(df[col_name].values, bins="auto")
        plt.title('{}'.format(Counter(str_vals)))
        plt.show()

    # Error checking
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    # Creating the X values
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    X = df_vals.values
    y = df[col_name].values

    return X, y, df


src = 'S&P500_joined_adj-close.csv'
ticker = "AAPL"
num_days = 7
