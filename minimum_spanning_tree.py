import sys
from typing import Set, List


class Edge:

    def __init__(self, from_ind, to_ind):
        self.from_ind = from_ind
        self.to_ind = to_ind

    def __eq__(self, obj):
        return (self.from_ind, self.to_ind) == (obj.from_ind, obj.to_ind) or (self.from_ind, self.to_ind) == (obj.to_ind, obj.from_ind)

    def __hash__(self):
        if self.from_ind > self.to_ind:
            return hash(str(self.from_ind) + "-" + str(self.to_ind))
        return hash(str(self.to_ind) + "-" + str(self.from_ind))

    def __str__(self):
        return "from_ind: " + str(self.from_ind) + " | " + "to_ind: " + str(self.to_ind) + "\n"

    def to_set(self):
        return {self.from_ind, self.to_ind}


def prims(graph):
    min_spanning_tree = [[None for i in range(len(graph))] for j in range(len(graph))]
    min_edge, min_edge_val = find_minimum_edge(graph)
    print(min_edge, min_edge_val)

    min_spanning_tree[min_edge.from_ind][min_edge.to_ind] = min_edge_val
    min_spanning_tree[min_edge.to_ind][min_edge.from_ind] = min_edge_val
    min_spanning_tree_edges = {min_edge}
    min_spanning_tree_vertices = min_edge.to_set()

    for i in range(len(graph) - 1):
        min_edge, min_edge_val = find_minimum_edge_from_vertex(graph, min_spanning_tree_edges, min_spanning_tree_vertices, min_spanning_tree)
        if min_edge is None:
            for i in min_spanning_tree:
                print(i)
        else:
            "done"
        min_spanning_tree[min_edge.from_ind][min_edge.to_ind] = min_edge_val
        min_spanning_tree[min_edge.to_ind][min_edge.from_ind] = min_edge_val
        min_spanning_tree_edges.add(min_edge)
        min_spanning_tree_vertices.union(min_edge.to_set())
    for i in min_spanning_tree:
        print(i)
    return min_spanning_tree


def find_minimum_edge_from_vertex(graph, existing_edges, min_spanning_tree_vertices, min_spanning_tree):
    min_edge_val = sys.maxsize
    min_edge = None
    for i in min_spanning_tree_vertices:
        for j in range(len(graph)):
            if graph[i][j] is None:
                continue
            if Edge(i, j) not in existing_edges and graph[i][j] < min_edge_val:
                temp_tree = min_spanning_tree
                temp_tree[i][j] = graph[i][j]
                temp_tree[j][i] = graph[i][j]
                if not has_cycle(temp_tree):
                    min_edge_val = graph[i][j]
                    min_edge = Edge(i, j)
    return min_edge, min_edge_val


def find_minimum_edge(graph):
    min_edge = None
    min_edge_val = sys.maxsize
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] is None:
                continue
            if graph[i][j] < min_edge_val:
                min_edge = Edge(i, j)
                min_edge_val = graph[i][j]
    return min_edge, min_edge_val


def has_cycle(graph):
    for i in range(len(graph)):
        visited = {i}
        edges = set()
        if track_cycle(graph, visited, edges, i):
            return True
    return False


def track_cycle(graph: List[List[int]], visited: Set[int], edges: Set[Edge], i) -> bool:
    for j in range(len(graph)):
        if graph[i][j] is None:
            continue
        if graph[i][j] > 0 and Edge(i, j) not in edges:
            if j in visited:
                return True
            else:
                visited.add(j)
                edges.add(Edge(i, j))
                return track_cycle(graph, visited, edges, j)
    return False


if __name__ == '__main__':
    graph2 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
    ]
    # edges = set()
    # print(track_cycle(graph2, {0}, edges, 0))

    m = None
    graph = [
        # a  b  c  d  e  f
        [m, 3, m, m, 6, 5],  # a
        [3, m, 1, m, m, 4],  # b
        [m, 1, m, 6, m, 4],  # c
        [m, m, 6, m, 8, 5],  # d
        [6, m, m, 8, m, 2],  # e
        [5, 4, 4, 5, 2, m]  # f
    ]
    prims(graph)
