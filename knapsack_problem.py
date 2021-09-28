from typing import List


class Item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value


def knapsack_problem_nomem(wv: List[Item], capacity, s=None):
    if s == len(wv) or capacity <= 0:
        return 0

    if s is None:
        s = 0
    for i in range(s, len(wv)):
        if wv[i].get_weight() > capacity:
            return knapsack_problem_nomem(wv, capacity, s + 1)
        else:
            return max(wv[i].get_value() + knapsack_problem_nomem(wv, capacity - wv[i].get_weight(), s + 1),
                       knapsack_problem_nomem(wv, capacity, s + 1))


def knapsack_problem(wv: List[Item], I, J, dp=None):
    if dp is None:
        dp = []
        for i in range(len(wv) + 1):
            dp.append([])
            for j in range(capacity + 1):
                if i == 0 or j == 0:
                    dp[i].append(0)
                else:
                    dp[i].append(-1)

    if dp[I][J] != -1:
        return dp[I][J]

    if wv[I - 1].get_weight() > J:
        max_val = knapsack_problem(wv, I - 1, J, dp)
    else:
        max_val = max(
            wv[I - 1].get_value() + knapsack_problem(wv, I - 1, J - wv[I - 1].get_weight(), dp),
            knapsack_problem(wv, I - 1, J, dp)
        )
    dp[I][J] = max_val
    return max_val


def sort_on_weight(wv: List[Item]) -> List[Item]:
    return sorted(wv, key=lambda item: item.get_weight())


if __name__ == '__main__':
    wv = [Item(2, 12), Item(1, 10), Item(3, 20), Item(2, 15)]
    capacity = 5
    # print(knapsack_problem_nomem(wv, capacity))
    print(knapsack_problem(wv, 4, 5))
