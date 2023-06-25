# -*- coding: utf-8 -*-
import pandas as pd


def main():
    df = pd.read_csv("http://logopt.com/data/iris.data", names=["がく片長", "がく片幅", "花びら長", "花びら幅", "種類"])
    df2 = df.drop("がく片長", axis=1)
    print(df2.drop([3,5], axis=0))



if __name__ == '__main__':
    main()
