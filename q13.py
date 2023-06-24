# -*- coding: utf-8 -*-
import numpy as np


def main():
    for i in range(1, 10):
        print(f"{i}: {f(i)}")


def f(x):
    """x>=1の整数とする。1または素数の時にTrueを返す。"""
    return not np.any([x % i == 0 for i in range(2, x)])


if __name__ == '__main__':
    main()
