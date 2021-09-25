from sorting import is_sorted


def heap_sort(array):
    sorted_array = []
    array = heap_bottom_up(array)
    while len(array) > 1:
        sorted_array.append(array[0])
        array[0] = array[-1]
        array = array[:-1]
        array = heapify(array, 0)
    return sorted_array


def heap_bottom_up(array):
    first_node_with_child = int((len(array) - 3) / 2)
    for i in range(first_node_with_child, -1, -1):
        array = heapify(array, i)
    return array


def heapify(array, n):
    c1 = (2 * n) + 1
    c2 = (2 * n) + 2

    # No child
    if c1 >= len(array) or c2 >= len(array):
        return array
    # One child
    if c1 == len(array):
        if array[c1] < array[n]:
            array[c1], array[n] = array[n], array[c1]
            return heapify(array, c1)
        return array
    # Node lesser than equal to children
    if array[n] <= array[c1] and array[n] <= array[c2]:
        return array
    # One or both children are greater than node
    if array[c2] <= array[c1]:
        array[c2], array[n] = array[n], array[c2]
        return heapify(array, c2)
    # c1 is smallest
    array[c1], array[n] = array[n], array[c1]
    return heapify(array, c1)


def is_heap(array):
    i = 0
    while i < len(array):
        c1 = (2 * i) + 1
        c2 = (2 * i) + 2

        if (c1 < len(array) and array[c1] < array[i]) or (c2 < len(array) and array[c2] < array[i]):
            return False
        i += 1
    return True


if __name__ == '__main__':
    array = [9, 5, 7, 2, 8, 3, 11, 19, 15, 1, 12, 14, 2, 5, 9, 11, 3]
    print(is_heap(array))
    print(is_heap(heap_bottom_up(array)))
    print(is_sorted(heap_sort(array)))
