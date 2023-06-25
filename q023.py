# -*- coding: utf-8 -*-
import pandas as pd


def main():
    drinks = pd.read_csv("http://logopt.com/data/drinks.csv")
    print(drinks.head())
    print(drinks.groupby("country")[["beer_servings", "spirit_servings", "wine_servings"]].agg("mean"))


if __name__ == '__main__':
    main()
