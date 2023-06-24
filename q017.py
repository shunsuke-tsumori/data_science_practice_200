# -*- coding: utf-8 -*-
import pandas as pd


def main():
    df = pd.read_csv("http://logopt.com/data/vgsales.csv")
    print(df.head())


if __name__ == '__main__':
    main()
