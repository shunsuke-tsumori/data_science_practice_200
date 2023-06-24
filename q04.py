# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = np.ones((3, 3))
    print(x[1][0])
    print(x[1])
    print(x[:2, 1:])
    print(x[::2,::2])
    print(x + y)
    print(x * y)
    print(x * 1)
    print(x * np.array([1,1,1]))


if __name__ == '__main__':
    main()
