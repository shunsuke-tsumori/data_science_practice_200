# -*- coding: utf-8 -*-
import numpy as np


def main():
    np.random.seed(1)
    demand = np.random.normal(100, 10, 10)
    print(demand)

    q = 110
    cost = np.where(demand > q, (demand - q) * 100, q - demand)
    print(cost)
    print(cost.sum())

    min_q = 0
    min_q_value = 10 ** 15
    for q in range(1000):
        cost = np.where(demand > q, (demand - q) * 100, q - demand)
        cc = cost.sum()
        if cc < min_q_value:
            min_q = q
            min_q_value = cc
    print(min_q)
    print(min_q_value)


if __name__ == '__main__':
    main()
