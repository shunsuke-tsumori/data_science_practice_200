# -*- coding: utf-8 -*-
import pandas as pd


def main():
    df = pd.read_csv("http://logopt.com/data/iris.data", names=["がく片長", "がく片幅", "花びら長", "花びら幅", "種類"])
    print(df[df["花びら幅"] < 0.5])
    print(df[(df["花びら幅"] < 0.5)& (df["花びら長"] < 1.5)])
    df2 = df[df["種類"]=="Iris-setosa"]
    df3 = df[df["種類"]=="Iris-versicolor"]
    df4 = df[df["種類"]=="Iris-virginica"]
    print(df2.describe())
    print(df3.describe())
    print(df4.describe())



if __name__ == '__main__':
    main()
