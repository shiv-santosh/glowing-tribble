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
    array = [12, 543, 123, 6565, 876, 123, 5454, 6, 451234, 6565, 234, 4357867, 345, 345]
    print(is_heap(array))
