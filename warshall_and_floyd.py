import sys


def warshall(graph):
    # a[i][j] path exists from i -> j
    l = len(graph)
    for i in range(l):  # highlight
        for j in range(l):  # each in highlight
            for k in range(l):  # check path
                # each highlight - a[i][j]
                # each to compare - a[k][i]
                # possible change - a[k][j]
                graph[k][j] = int(bool(graph[k][j]) or (bool(graph[k][i] and graph[i][j])))
    for i in graph:
        print(i)


def floyd(graph):
    # a[i][j] path exists from i -> j
    l = len(graph)
    for i in range(l):  # highlight
        for j in range(l):  # each in highlight
            for k in range(l):  # check path
                # each highlight - a[i][j]
                # each to compare - a[k][i]
                # possible change - a[k][j]
                graph[k][j] = min(graph[k][j], graph[k][i] + graph[i][j])
    for i in graph:
        print(i)


if __name__ == '__main__':
    # graph = [
    #     [0, 1, 0, 0],
    #     [0, 0, 0, 1],
    #     [0, 0, 0, 0],
    #     [1, 0, 1, 0]
    # ]
    m = sys.maxsize
    graph = [
        [0, m, 3, m],
        [2, 0, m, m],
        [m, 7, 0, 1],
        [6, m, m, 0]
    ]
    floyd(graph)
