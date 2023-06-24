# -*- coding: utf-8 -*-
import numpy as np


def main():
    np.random.seed(1)
    T = 1000
    s = 120
    S = 150
    n = 10

    I = np.zeros((n, T + 1))
    D = np.random.normal(100, 10, size=(n, T + 1))
    Q = np.zeros((n, T + 1))

    for t in range(1, T + 1):
        Q[:, t] = np.where(I[:, t - 1] < s, S - I[:, t - 1], 0)
        I[:, t] = I[:, t - 1] + Q[:, t] - D[:, t]
    print(Q)
    print(I)


if __name__ == '__main__':
    main()
