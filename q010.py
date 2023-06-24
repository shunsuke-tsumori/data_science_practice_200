# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.array([1, 2, 3, 4, 5, 6])
    print(x[[0, 5]])
    print(x[x % 2 == 0])
    print(x[x % 2 != 0] * 2)


if __name__ == '__main__':
    main()
