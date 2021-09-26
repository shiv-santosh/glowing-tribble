def generate_lexicographic_perms(n):
    perms = []
    perm = [i for i in range(1, n + 1)]
    perms.append(perm)
    while True:
        lc = get_last_consecutive_ordered_elements(perm)
        if lc == -1:
            break
        index_to_switch = get_index_to_switch(perm, lc)
        perm[index_to_switch], perm[lc] = perm[lc], perm[index_to_switch]
        perm = invert(perm, lc + 1)
        perms.append(perm)
    print_perms(perms)


def print_perms(perms):
    for i in perms:
        print(" ".join([str(j) for j in i]))


def invert(perm, invert_start):
    return perm[:invert_start] + perm[invert_start:][::-1]


def get_index_to_switch(perm, lc):
    for i in range(len(perm) - 1, lc, -1):
        if perm[i] > perm[lc]:
            return i
    return -1


def get_last_consecutive_ordered_elements(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            return i
    return -1


if __name__ == '__main__':
    generate_lexicographic_perms(4)
