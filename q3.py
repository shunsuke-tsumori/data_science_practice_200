# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.array([1, 2, 3])
    y = np.array([5, 6, 7])
    print(x + y)
    print(x[:2] + y[-2:])
    print(x + 10)
    print(y ** 3)
    print(x * y)


if __name__ == '__main__':
    main()
