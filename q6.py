# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.arange(100)
    print(np.sin(x))
    y = np.arange(1, 1000)
    print(np.log(y * 2) + 100)


if __name__ == '__main__':
    main()
