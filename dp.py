def coin_row_problem_nomem(array, s):
    if s >= len(array):
        return 0
    if len(array) - 1 == s:
        return array[len(array) - 1]
    if len(array) - 2 == s:
        return max(array[len(array) - 1], array[len(array) - 2])
    return max(array[s] + coin_row_problem_nomem(array, s + 2), coin_row_problem_nomem(array, s + 1))


def coin_row_problem(array, s, dp):
    if s >= len(array):
        return 0
    if len(array) - 1 == s:
        return array[len(array) - 1]
    if len(array) - 2 == s:
        return max(array[len(array) - 1], array[len(array) - 2])

    if dp[s] != -1:
        return dp[s]
    max_coins_at_s = max(array[s] + coin_row_problem(array, s + 2, dp), coin_row_problem(array, s + 1, dp))
    dp[s] = max_coins_at_s
    return max_coins_at_s


if __name__ == '__main__':
    array = [5, 1, 2, 10, 6, 2]

    dp = [-1] * len(array)
    print(coin_row_problem(array, 0, dp))
