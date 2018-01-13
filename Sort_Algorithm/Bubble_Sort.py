# -*- encoding:utf-8 -*-
# __author__=='Gan'

from Sort_Algorithm.utils import decorator_timer, generate_array


def bubble_sort(array):
    is_sorted = False
    last_unsorted = len(array) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        last_unsorted -= 1  # After iteration last one became the largest one, so we don't need to handle it again.

    return array


@decorator_timer
def main(array):
    return bubble_sort(array)


if __name__ == '__main__':
    array = generate_array()
    main(array)
