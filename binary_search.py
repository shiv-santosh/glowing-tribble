import random

from sorting import merge_sort


def binary_search(array, element):
    l = 0
    h = len(array) - 1
    while l <= h:
        mid = (l + h) // 2
        if array[mid] == element:
            return mid
        if array[mid] < element:
            l = mid + 1
        else:
            h = mid - 1
    return -1


if __name__ == '__main__':
    elements = []
    while len(elements) != 10:
        r = int((random.random() * 20) // 1)
        if r in elements:
            continue
        elements.append(r)
    to_find = int((random.random() * 10) // 1)
    elements = merge_sort(elements)
    print(binary_search(elements, elements[to_find]))
    print(elements[binary_search(elements, elements[to_find])] == elements[to_find])
