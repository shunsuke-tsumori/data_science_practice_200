# -*- coding: utf-8 -*-
import numpy as np


def main():
    a = np.array([[1, 0, 0], [-1, 1, 0], [0, -1, 1]])
    v = np.array([4, 5, 6])
    a.shape = (9, 1)
    print(a)
    v.shape = (3, 1)
    print(v)
    # a.shape = (4,2)


if __name__ == '__main__':
    main()
