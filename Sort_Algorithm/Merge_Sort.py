# -*- encoding:utf-8 -*-
# __author__=='Gan'

from Sort_Algorithm.utils import decorator_timer, generate_array


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


@decorator_timer
def main(array):
    result = merge_sort(array)
    return result


if __name__ == '__main__':
    main(generate_array())

