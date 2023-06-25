# -*- coding: utf-8 -*-
import pandas as pd


def main():
    ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)
    print(ufo.dtypes)
    ufo["Year"] = pd.to_datetime(ufo["Time"]).dt.year
    ufo["Weekday"] = pd.to_datetime(ufo["Time"]).dt.weekday
    print(ufo.head())

    print(ufo[ufo["Year"] >= 2000])


if __name__ == '__main__':
    main()
a
