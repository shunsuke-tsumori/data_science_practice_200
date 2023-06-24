# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.random.randint(1, 7, size=10)
    print(x)
    y = np.random.normal(100, 10, size=(10, 10))
    print(y)


if __name__ == '__main__':
    main()
