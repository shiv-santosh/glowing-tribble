def bubble_sort(array):
    for j in range(len(array) - 1, -1, -1):
        swapped = False
        for i in range(j):
            if array[i] > array[i + 1]:
                swapped = True
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        if not swapped:
            return array
    return array


def recursive_bubble_sort(array, n=None):
    if n is None:
        n = len(array)
    if n < 0 or n > len(array):
        return array
    swapped = False
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            swapped = True
            temp = array[i + 1]
            array[i + 1] = array[i]
            array[i] = temp
    if not swapped:
        return array
    return recursive_bubble_sort(array, n - 1)


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0:
            if array[j] < array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
            else:
                break
            j -= 1
    return array


def recursive_insertion_sort(array, n=None):
    if n is None:
        n = 1
    elif n == len(array):
        return array
    i = n
    while i > 0:
        if array[i] >= array[i - 1]:
            break
        temp = array[i - 1]
        array[i - 1] = array[i]
        array[i] = temp
    return array


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = int(len(array) / 2)

    first_half = merge_sort(array[:mid])
    second_half = merge_sort(array[mid:])

    array = [None] * (len(first_half) + len(second_half))
    fi = 0
    si = 0
    i = 0
    while fi < len(first_half) or si < len(second_half):
        if fi == len(first_half):
            array[i] = second_half[si]
            si += 1
        elif si == len(second_half):
            array[i] = first_half[fi]
            fi += 1
        elif first_half[fi] > second_half[si]:
            array[i] = second_half[si]
            si += 1
        else:
            array[i] = first_half[fi]
            fi += 1
        i += 1
    return array


def iterative_merge_sort(array):
    window = 1
    while window < len(array):
        for i in range(0, len(array), window * 2):
            start = i
            mid = i + window
            if mid > len(array):
                continue
            end = min(mid + window, len(array))
            sorted_segment = [-1] * (end - start)
            fi = start
            si = mid
            ssi = 0
            while fi < mid or si < end:
                if fi == mid:
                    sorted_segment[ssi] = array[si]
                    si += 1
                    ssi += 1
                elif si == end:
                    sorted_segment[ssi] = array[fi]
                    fi += 1
                    ssi += 1
                elif array[fi] <= array[si]:
                    sorted_segment[ssi] = array[fi]
                    ssi += 1
                    fi += 1
                else:
                    sorted_segment[ssi] = array[si]
                    si += 1
                    ssi += 1
            ssi = 0
            for j in range(start, end):
                array[j] = sorted_segment[ssi]
                ssi += 1

        window = window * 2

    return array


def quick_sort(array, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(array)
    if end - start <= 1:
        return array

    partition = end - 1

    li = start
    ri = end - 1
    while li < ri:
        if array[li] <= array[partition]:
            li = li + 1
            continue
        if array[ri] > array[partition]:
            ri = ri - 1
            continue
        array[li], array[ri] = array[ri], array[li]
    partition = ri
    quick_sort(array, start, partition)
    quick_sort(array, partition + 1, end)
    return array


def iterative_quick_sort(array):
    stack = [(0, len(array))]
    while bool(stack):
        cur = stack[-1]
        stack = stack[:-1]
        if cur[1] - cur[0] <= 1:
            continue

        li = cur[0]
        pivot = array[cur[1] - 1]
        ri = cur[1] - 1
        while li < ri:
            if array[li] <= pivot:
                li = li + 1
                continue
            if array[ri] > pivot:
                ri = ri - 1
                continue
            array[li], array[ri] = array[ri], array[li]
        pivot = ri
        stack = stack + [(cur[0], pivot), (pivot, cur[1])]
    return array


if __name__ == '__main__':
    array = [12, 543, 123, 6565, 876, 123, 5454, 6, 451234, 6565, 234, 4357867, 345, 345]
    print(array)
    array = iterative_quick_sort(array)
    print(array)
    print(is_sorted(array))

