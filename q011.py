# -*- coding: utf-8 -*-
import numpy as np


def main():
    dice1 = np.random.randint(1, 7, 10)
    print(dice1)
    print(dice1[dice1 >= 4])
    dice2 = np.random.randint(1, 7, 100)
    print(dice2)
    print(dice2[(dice2 >= 5) & (dice2 % 2 != 0)])
    m = np.random.normal(10, 10, size=(10, 10))
    print(m)
    print(m[m < 0])


if __name__ == '__main__':
    main()
