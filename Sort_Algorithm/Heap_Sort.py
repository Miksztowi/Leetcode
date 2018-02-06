# -*- encoding:utf-8 -*-
# __author__=='Gan'

from Sort_Algorithm.utils import decorator_timer, generate_array


def fixdown(a, k, n):
    N = n - 1
    while k * 2 <= N:
        j = 2 * k
        if j < N and a[j] < a[j + 1]:
            j += 1
        if a[k] < a[j]:
            a[k], a[j] = a[j], a[k]
            k = j
        else:
            break


def heapSort(l):
    n = len(l) - 1
    for i in range(n // 2, 0, -1): # i取0会有异常， 字节点 l = 2 * i,r = 2 * i,所以为0时i = l = r.
        fixdown(l, i, len(l))
    while n > 1:
        l[1], l[n] = l[n], l[1]
        fixdown(l, 1, n)
        n -= 1
    return l[1:] # 从array的下标1后开始取结果，下标0为占位，无实际意义。


@decorator_timer
def main(array):
    heapSort(array)
    return array


if __name__ == '__main__':
    array = generate_array()
    main(array)
