# -*- coding: utf-8 -*-
import numpy as np


def main():
    a = np.ones(10)
    print(a)
    b = np.ones((3, 4))
    print(b)
    c = np.zeros((3, 3))
    for i in range(3):
        c[i, 2 - i] = 1.0
    print(c)
    d = np.zeros((10, 10))
    for i in range(9):
        d[i, i + 1] = 1.0
    print(d)


if __name__ == '__main__':
    main()
