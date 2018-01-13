# -*- encoding:utf-8 -*-
# __author__=='Gan'

from Sort_Algorithm.utils import decorator_timer, generate_array


def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left


def quick_sort(array, left, right):
    if left >= right:
        return
    pivot = array[(left + right) // 2]
    index = partition(array, left, right, pivot)
    quick_sort(array, left, index - 1)
    quick_sort(array, index, right)


@decorator_timer
def main(array):
    quick_sort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    array = generate_array()
    main(array, 0, len(array) - 1)
