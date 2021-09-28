import sys


def coin_row_problem_nomem(array, s):
    if s >= len(array):
        return 0
    if len(array) - 1 == s:
        return array[len(array) - 1]
    if len(array) - 2 == s:
        return max(array[len(array) - 1], array[len(array) - 2])
    return max(array[s] + coin_row_problem_nomem(array, s + 2), coin_row_problem_nomem(array, s + 1))


def coin_row_problem(array, s, dp=None):
    if dp is None:
        dp = [-1] * len(array)
        dp[len(array) - 1] = array[len(array) - 1]
        dp[len(array) - 2] = max(array[len(array) - 1], array[len(array) - 2])

    if s >= len(array):
        return 0

    if dp[s] != -1:
        return dp[s]

    max_coins_at_s = max(array[s] + coin_row_problem(array, s + 2, dp), coin_row_problem(array, s + 1, dp))
    dp[s] = max_coins_at_s
    return max_coins_at_s


def change_making_problem_nomem(coins, total):
    min_req = sys.maxsize
    for i in coins:
        if i < total:
            min_req = min(1 + change_making_problem_nomem(coins, total - i), min_req)
        elif i == total:
            return 1
    return min_req


def change_making_problem(coins, total, dp=None):
    if dp is None:
        dp = [-1] * (total + 1)
    if dp[total] != -1:
        return dp[total]

    min_req = sys.maxsize
    for i in coins:
        if i < total:
            min_req = min(1 + change_making_problem(coins, total - i, dp), min_req)
        elif i == total:
            dp[total] = 1
            return 1
    dp[total] = min_req
    return min_req


def robot_coin_collection_nomem(graph, i=None, j=None):
    if i is None and j is None:
        i = 0
        j = 0
    if i + 1 == len(graph) and j + 1 == len(graph[i]):
        return graph[i][j]

    return graph[i][j] + max(
        robot_coin_collection_nomem(graph, i + 1, j) if i + 1 < len(graph) else 0,
        robot_coin_collection_nomem(graph, i, j + 1) if j + 1 < len(graph[i]) else 0
    )


def robot_coin_collection(graph):
    l = len(graph[0])
    w = len(graph)

    coins_total = []
    for i in range(w):
        coins_total.append([])
        for j in range(l):
            coins_total[i].append(0)

    for i in range(1, l):
        coins_total[0][i] = graph[0][i - 1] + graph[0][i]

    for j in range(1, w):
        coins_total[j][0] = graph[j][0] + graph[j - 1][0]

    for i in range(1, l):
        for j in range(1, w):
            coins_total[j][i] = graph[j][i] + max(coins_total[j - 1][i], coins_total[j][i - 1])
    return coins_total[w - 1][l - 1]


if __name__ == '__main__':
    # array = [5, 1, 2, 10, 6, 2]
    # print(coin_row_problem(array, 0))

    # coins = [1, 3, 4]
    # total = 6
    # print(change_making_problem(coins, total))

    graph = [
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0]
    ]
    print(robot_coin_collection(graph))
