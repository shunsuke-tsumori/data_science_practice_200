# -*- coding: utf-8 -*-
import string

import pandas as pd


def main():
    headers = [string.ascii_lowercase[i] for i in range(9)]
    df = pd.read_csv("http://logopt.com/data/auto-mpg.data", names=headers, delim_whitespace=True)
    print(df.sort_values("f", ascending=False))
    print("------------")
    print(df.sort_values("e", ascending=False))


if __name__ == '__main__':
    main()
