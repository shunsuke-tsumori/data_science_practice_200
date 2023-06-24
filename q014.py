# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def main():
    xs = np.arange(1, 101, 3)
    print(xs)
    plt.plot(xs, np.sqrt(xs))
    plt.show()

    xs2 = np.linspace(0.1, 10, 1000)
    plt.plot(xs2, 1 / xs2)
    plt.show()


if __name__ == '__main__':
    main()
