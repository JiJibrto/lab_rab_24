#!/usr/bin/env python3
# -*- config: utf-8 -*-

# 7 и 24

import math
from threading import Thread


def sm_first(x, n):
    return ((-1) ** (n + 1) * math.sin(n) * x) / n


def first(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_first(x, n)
    n += 1
    test = x / 2

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_first(x, n)
        n += 1
        print(n)

    current = round(current, 6)
    test = round(test, 6)
    print(f'Сумма ряда {current} ~ проверочному значению {test}')


def sm_second(x, n):
    return ((-1) ** n) * x ** (2 * n) / math.factorial(2 * n)


def second(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_second(x, n)
    n += 1
    test = math.cos(x)

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_second(x, n)
        n += 1
        print(n)

    current = round(current, 6)
    test = round(test, 6)
    if current == test:
        print(f'Сумма ряда {current} = проверочному значению {test}')


if __name__ == '__main__':
    th2 = Thread(target=second(0.3, 0))
    th1 = Thread(target=first(-(math.pi/2), 1))

    th1.start()
    th2.start()
