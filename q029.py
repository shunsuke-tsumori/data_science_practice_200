# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd


def main():
    movie = pd.read_csv("http://logopt.com/data/movie_metadata.csv")
    print(movie.head())

    jonny = movie[movie["actor_1_name"]=="Johnny Depp"]
    print(jonny.head())
    pt = jonny.pivot_table(index="title_year", values=["budget", "gross"], aggfunc="sum")
    pt.plot()
    plt.show()



if __name__ == '__main__':
    main()
