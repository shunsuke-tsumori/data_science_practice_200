# -*- coding: utf-8 -*-
import numpy as np
def main():
    a = np.arange(25)
    a.shape = (5,5)
    print(a)
    print(a[1::3,::2])
    print(a[::2,:4:2])


if __name__ == '__main__':
    main()
