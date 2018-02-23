# -*- encoding:utf-8 -*-
# __author__=='Gan'

from Sort_Algorithm.utils import decorator_timer, generate_array


def insert_sort(arrary):
    for i in range(1, len(arrary)):
        j = i - 1
        key = arrary[i]
        while j >= 0 and key < arrary[j]:
            arrary[j + 1] = arrary[j]
            j -= 1
            arrary[j + 1] = key
    return arrary


@decorator_timer
def main(array):
    result = insert_sort(array)
    return result


if __name__ == '__main__':
    main(generate_array())
