# -*- coding: utf-8 -*-
import pandas as pd


def main():
    ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)
    print(ufo.head())
    ufo["City"].fillna("場所不明", inplace=True)
    ufo["Colors Reported"].fillna("たぶん白", inplace=True)
    print(ufo.head())


if __name__ == '__main__':
    main()
