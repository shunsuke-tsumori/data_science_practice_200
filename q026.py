# -*- coding: utf-8 -*-
import pandas as pd


def main():
    drinks = pd.read_csv("http://logopt.com/data/drinks.csv", dtype={
        "beer_servings": float,
        "spirit_servings": float,
        "wine_servings": float
    })
    print(drinks.dtypes)

    drinks["continent"] = drinks["continent"].replace("Asia", "アジア")
    print(drinks.head(50))


if __name__ == '__main__':
    main()
