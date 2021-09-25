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


if __name__ == '__main__':
    s1 = "askjdghaskjdhkavsflasgudlgasd"
    s2 = "askjdghaskjdhkavsflasgudlgasd"
    print(is_matching(s1, s2))
