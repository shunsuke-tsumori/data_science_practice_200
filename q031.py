# -*- coding: utf-8 -*-
import pandas as pd


def main():
    ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)
    ufo = ufo.rename(columns={"State": "州", "Colors Reported": "色"})
    print(ufo.head())


if __name__ == '__main__':
    main()
