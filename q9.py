# -*- coding: utf-8 -*-
import numpy as np
def main():
    a = np.random.randint(low=1, high=100, size=(3,5))
    print(a)
    print(np.min(a, axis=1))
    print(np.min(a, axis=0))

    dice = np.random.randint(1, 7, 10)
    print(dice)
    print(np.min(dice))
    print(np.max(dice))
    print(np.average(dice))

    sq = np.random.normal(10, 10, size=(10, 10))
    print(sq)
    print(np.average(sq))
    print(np.average(sq, axis=1))


if __name__ == '__main__':
    main()
