# -*- coding: utf-8 -*-
import string

import pandas as pd


def main():
    headers = [string.ascii_lowercase[i] for i in range(9)]
    df = pd.read_csv("http://logopt.com/data/auto-mpg.data", names=headers, delim_whitespace=True)
    print(df.head())
    print(df.tail())


if __name__ == '__main__':
    main()
