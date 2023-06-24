# -*- coding: utf-8 -*-
import string

import pandas as pd


def main():
    column = [string.ascii_lowercase[i] for i in range(14)]
    df = pd.read_csv(
        "http://logopt.com/data/wine.data",
        names=column
    )
    print(df.head())


if __name__ == '__main__':
    main()
