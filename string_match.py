def is_matching(s1, s2):
    s1l = list(s1)
    s2l = list(s2)

    ls1 = len(s1)
    ls2 = len(s2)

    if ls1 != ls2:
        return False

    for i in range(len(s1l)):
        if s1l[i] != s2l[i]:
            return False
    return True


def horse_pool_algorithm(ip, s):
    tab = shift_table(s)
    ipl = list(ip)
    sl = list(s)

    pi = len(s) - 1
    si = len(s) - 1
    while si > 0 and pi < len(ip):
        if ipl[pi] == sl[si]:
            si -= 1
            pi -= 1
        else:
            si = len(s) - 1
            pi += tab.get(ipl[pi], len(s))
    if si <= 0:
        return pi
    return -1


def shift_table(string):
    f = {}
    l = len(string)
    sl = list(string)
    for i in range(l):
        f[sl[i]] = l - 1 - i
    return f


if __name__ == '__main__':
    s1 = "abcabcabcabcdabcabcabcabcabcabcabcabcabcabc"
    s2 = "abcd"
    print(horse_pool_algorithm(s1, s2))
