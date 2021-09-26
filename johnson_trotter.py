def johnson_trotter(n):
    perms = []
    f = []
    for i in range(1, n + 1):
        f.append([i, True])

    perms.append(get_permutation(f))
    while True:
        largest_movable = get_largest_movable(f)
        if largest_movable < 0:
            break
        moved = f[largest_movable][0]
        move_largest(f, largest_movable)
        reverse_larger_members(f, moved)
        perms.append(get_permutation(f))
    print_perms(perms)


def print_with_direction(f):
    s1 = ""
    s2 = ""
    for i in f:
        if i[1]:
            s1 += "<-\t"
        else:
            s1 += "->\t"
        s2 += str(i[0]) + "\t"
    print(s1)
    print(s2)


def print_perms(perms):
    for i in perms:
        print(" ".join(i))


def get_permutation(f):
    s = ""
    for i in f:
        s += str(i[0])
    return s


def move_largest(f, largest_movable):
    move = largest_movable - 1 if f[largest_movable][1] else largest_movable + 1
    f[move], f[largest_movable] = f[largest_movable], f[move]


def reverse_larger_members(f, m):
    for i in range(len(f)):
        if f[i][0] > m:
            f[i][1] = not f[i][1]
    return f


def get_largest_movable(f):
    largest_movable = -1
    for i in range(len(f)):
        v = f[i][0]
        d = f[i][1]
        if d:
            if i - 1 < 0:
                continue
            else:
                if f[i-1][0] < v and (largest_movable == -1 or f[largest_movable][0] < v):
                    largest_movable = i
        else:
            if i + 1 >= len(f):
                continue
            else:
                if f[i + 1][0] < v and (largest_movable == -1 or f[largest_movable][0] < v):
                    largest_movable = i

    return largest_movable


if __name__ == "__main__":
    johnson_trotter(4)
    # print(get_largest_movable([[2, True], [1, True], [3, False], [4, False]]))
