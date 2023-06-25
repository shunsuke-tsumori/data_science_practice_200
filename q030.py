# -*- coding: utf-8 -*-
import pandas as pd


def main():
    poke = pd.read_csv("http://logopt.com/data/Pokemon.csv", index_col=0)
    x = poke[poke["Legendary"] & (poke["Attack"]<poke["Defense"]) & (poke["Attack"] <= 90) & (poke["Speed"] >= 110)]
    print(x["Name"])


if __name__ == '__main__':
    main()
