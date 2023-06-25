# -*- coding: utf-8 -*-
import pandas as pd


def main():
    poke = pd.read_csv("http://logopt.com/data/Pokemon.csv", index_col=0)
    print(poke.head())
    x = poke.pivot_table(index=["Type 1", "Generation"], values=["Attack", "Defense"], aggfunc=["mean"])
    print(x)


if __name__ == '__main__':
    main()
