# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("http://logopt.com/data/iris.data", names=["がく片長", "がく片幅", "花びら長", "花びら幅", "種類"])
    print(df.iloc[5:9, 2:4])
    print("-------")
    print(df.loc[:,"種類"])
    print("-------")
    print(df.loc[[2,6,4], ["がく片長", "花びら幅", "花びら長"]])


if __name__ == '__main__':
    main()
