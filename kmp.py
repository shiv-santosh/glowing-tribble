class Solution:

    @staticmethod
    def kmp_search(text: str, pattern: str):
        if len(pattern) == 1:
            for i in range(len(text)):
                if pattern == text[i]:
                    return i
        helper = Solution.build_kmp_helper(pattern)
        p = 0
        t = 0
        while t < len(text):
            if pattern[p] == text[t]:
                t += 1
                p += 1
                if p == len(pattern):
                    return t - len(pattern)
            else:
                if p == 0:
                    t += 1
                else:
                    p = helper[p - 1]
        return -1

    @staticmethod
    def build_kmp_helper(pattern):
        helper = [0] * len(pattern)
        f = 0
        s = 1
        while s < len(pattern):
            if pattern[f] == pattern[s]:
                helper[s] = f + 1
                f += 1
                s += 1
            else:
                if f != 0:
                    while f != 0 and pattern[f] != pattern[s]:
                        f = helper[f - 1]
                else:
                    s += 1
        return helper


if __name__ == '__main__':
    s = Solution()
    print(s.build_kmp_helper('abcaby'))
    print(s.kmp_search('abxabcabyabc', 'abcaby'))
