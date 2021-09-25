import sys


def distance(p1, p2):
    return pow(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2), 0.5)


def get_closest_pair(x, y):
    min_dist = sys.maxsize
    min_dist_pair = None
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            temp_dist = distance((x[i], y[i]), (x[j], y[j]))
            if temp_dist < min_dist:
                min_dist_pair = (x[i], y[i]), (x[j], y[j])
                min_dist = temp_dist
    return min_dist_pair, min_dist


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5, 6, 7, 1.5]
    y = [1, 2, 3, 4, 5, 6, 7, 1.5]
    print(get_closest_pair(x, y))
