from typing import Optional

import sys


class DisjointSet:

    node_map = {}

    class Node:
        def __init__(self, data, rank, parent):
            self.parent = parent
            self.rank = rank
            self.data = data

        def __eq__(self, other):
            return self.data == other.data

    def make_set(self, data):
        node = self.Node(data, 0, None)
        node.parent = node
        self.node_map[data] = node

    def find_set_from_val(self, data) -> Optional[Node]:
        node = self.node_map.get(data)
        if node is None:
            return None
        return self.find_set(node)

    def find_set(self, node) -> Node:
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.find_set(node.parent)
        return node.parent

    def union(self, data1, data2):
        node1 = self.find_set_from_val(data1)
        node2 = self.find_set_from_val(data2)

        if node1 == node2:
            return

        if node1.rank >= node2.rank:
            node2.parent = node1
            node1.rank = node1.rank + (1 if node1.rank == node2.rank else 0)
        else:
            node1.parent = node2

    def different_set(self, data1, data2) -> bool:
        node1 = self.find_set_from_val(data1)
        node2 = self.find_set_from_val(data2)
        return node1.parent != node2.parent


class MapHeap:

    mapping = {}
    heap = []

    # entries: List[key, value]
    def __init__(self, entries):
        self.heap = sorted(entries, key = lambda entry: entry[1])
        i = 0
        for entry in self.heap:
            self.mapping[entry[0]] = i
            i += 1

    # extract min
    def extract_min(self):
        cur_min = self.heap[0]
        del self.mapping[cur_min[0]]
        if len(self.heap) == 1:
            self.heap.pop()
            return cur_min
        self.heap[0] = self.heap.pop()
        self.mapping[self.heap[0][0]] = 0
        # top down heapify
        self.heapify_top_down()
        return cur_min

    def heapify_top_down(self, position=0):
        c1 = (2 * position) + 1
        c2 = (2 * position) + 2
        if c1 < len(self.heap) and c2 < len(self.heap):
            if self.heap[c1][1] < self.heap[c2][1] and self.heap[c1][1] <  self.heap[position][1]:
                self.swap(c1, position)
                self.heapify_top_down(c1)
            elif self.heap[c2][1] < self.heap[c1][1] and self.heap[c2][1] <  self.heap[position][1]:
                self.swap(c2, position)
                self.heapify_top_down(c2)
        elif c1 < len(self.heap) and self.heap[c1][1] <  self.heap[position][1]:
            self.swap(c1, position)
            self.heapify_top_down(c1)

    def contains(self, key):
        return key in self.mapping

    def update(self, key, val):
        position = self.mapping[key]
        self.heap[position][1] = val
        self.heapify_bottom_up(position)

    def heapify_bottom_up(self, position):
        if position == 0:
            return
        parent = self.get_parent(position)
        if self.heap[parent][1] > self.heap[position][1]:
            self.swap(parent, position)
            self.heapify_bottom_up(parent)

    def swap(self, i, j):
        self.mapping[self.heap[i][0]] = j
        self.mapping[self.heap[j][0]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    @staticmethod
    def get_parent(index):
        return int((index - 1) / 2)

    def is_empty(self):
        return not bool(self.mapping)


class MinSpanningTree:

    class Edge:
        def __init__(self, from_v, to_v, val):
            self.from_v = from_v
            self.to_v = to_v
            self.val = val

        def __eq__(self, other):
            return min(self.from_v, self.to_v) == min(other.from_v, other.to_v) \
                   and max(self.from_v, self.to_v) == max(other.from_v, other.to_v) \
                   and self.val == other.val

        def __hash__(self):
            return hash((min(self.from_v, self.to_v), max(self.from_v, self.to_v)))

        def __ge__(self, other):
            return self.val >= other.val

        def __lt__(self, other):
            return self.val < other.val

        def __str__(self):
            return str(self.from_v) + " to " + str(self.to_v) + ": " + str(self.val)

    @staticmethod
    def primsOpt(graph, vertices):
        from minimum_spanning_tree import Edge
        edge_distance_list = []
        for from_v, to_v_map in graph.items():
            for to_v, distance in to_v_map.items():
                edge_distance_list.append([Edge(from_v, to_v), distance])
        magic_heap = MapHeap(edge_distance_list)
        edge_vertex_map = {}
        mst = {}
        # fi = magic_heap.heap[0][0]
        while not magic_heap.is_empty():
            min_edge, distance = magic_heap.extract_min()
            min_vertex = min_edge.from_ind
            if min_vertex in edge_vertex_map:
                MinSpanningTree.add_edge_obj(mst, edge_vertex_map.get(min_vertex))

            for to_v, weight in graph.get(min_vertex).items():
                cur_edge = MinSpanningTree.Edge(min_vertex, to_v, weight)

                if to_v not in magic_heap.mapping:
                    continue

                magic_heap.update(to_v, weight)

                if cur_edge.to_v not in edge_vertex_map:
                    edge_vertex_map[cur_edge.to_v] = cur_edge
                else:
                    edge_vertex_map[cur_edge.to_v] = cur_edge if cur_edge.val <= edge_vertex_map[cur_edge.to_v].val else edge_vertex_map[cur_edge.to_v]
        # print(fi)
        MinSpanningTree.print_graph(mst)
        return mst

    @staticmethod
    def kruskal(graph, vertices):
        disjoint_set = DisjointSet()
        for vertex in vertices:
            disjoint_set.make_set(vertex)
        edges = MinSpanningTree.get_non_decreasing_edges(graph)
        mst = {}
        for edge in edges:
            if disjoint_set.different_set(edge.from_v, edge.to_v):
                disjoint_set.union(edge.from_v, edge.to_v)
                MinSpanningTree.add_edge(mst, edge.from_v, edge.to_v, edge.val)
            else:
                # same disjoint set
                pass
        MinSpanningTree.print_graph(mst)
        return mst

    @staticmethod
    def print_graph(graph):
        total_cost = 0
        for e, k in graph.items():
            print(e, k)
            total_cost += sum(list(k.values()))
        print('total cost: ' + str(total_cost/2))
        print('\n')

    @staticmethod
    def get_non_decreasing_edges(graph):
        non_decreasing_edges = []
        edges_set = set()
        for from_vertex, edges in graph.items():
            for to_vertex, weight in edges.items():
                cur_edge = MinSpanningTree.Edge(from_vertex, to_vertex, weight)
                if cur_edge not in edges_set:
                    non_decreasing_edges.append(cur_edge)
                    edges_set.add(cur_edge)
        return sorted(non_decreasing_edges)

    @staticmethod
    def prims(graph, vertices):
        if len(vertices) <= 2:
            return graph
        mst = {}
        mst_v = set()
        for v in vertices:
            mst_v.add(v)
            break

        while len(mst_v) < len(vertices):
            min_to_add = MinSpanningTree.find_minimum_edge_vertex(graph, mst_v)
            mst_v.add(min_to_add[1])
            if min_to_add[0] not in mst:
                mst[min_to_add[0]] = {
                    min_to_add[1]: graph[min_to_add[0]][min_to_add[1]]
                }
            else:
                mst[min_to_add[0]][min_to_add[1]] = graph[min_to_add[0]][min_to_add[1]]

        return mst

    @staticmethod
    def find_minimum_edge_vertex(graph, mst_v):
        min_edge_weight = sys.maxsize
        mev = None
        for fv in mst_v:
            if graph.get(fv) is None:
                continue
            for tv, e in graph.get(fv).items():
                if tv in mst_v:
                    continue
                if e < min_edge_weight:
                    mev = (fv, tv)
                    min_edge_weight = e
        return mev

    @staticmethod
    def add_edge_obj(graph, edge: Edge):
        return MinSpanningTree.add_edge(graph, edge.from_v, edge.to_v, edge.val)

    @staticmethod
    def add_edge(graph, from_v, to_v, weight, done=False):
        if from_v not in graph:
            graph[from_v] = {
                to_v: weight
            }
        else:
            graph[from_v][to_v] = weight

        if not done:
            MinSpanningTree.add_edge(graph, to_v, from_v, weight, True)


if __name__ == '__main__':
    graph = {}
    MinSpanningTree.add_edge(graph, 'a', 'b', 3)
    MinSpanningTree.add_edge(graph, 'a', 'f', 5)
    MinSpanningTree.add_edge(graph, 'a', 'e', 6)

    MinSpanningTree.add_edge(graph, 'b', 'f', 4)
    MinSpanningTree.add_edge(graph, 'b', 'c', 1)

    MinSpanningTree.add_edge(graph, 'f', 'c', 4)
    MinSpanningTree.add_edge(graph, 'f', 'd', 5)
    MinSpanningTree.add_edge(graph, 'f', 'e', 2)

    MinSpanningTree.add_edge(graph, 'c', 'd', 6)

    MinSpanningTree.add_edge(graph, 'd', 'e', 8)

    # for i,v in graph.items():
    #     print(i, v)
    # MinSpanningTree.prims(graph, {'a', 'b', 'c', 'd', 'e', 'f'})
    # for edge in MinSpanningTree.get_non_decreasing_edges(graph):
    #     print(edge)
    MinSpanningTree.primsOpt(graph, {'a', 'b', 'c', 'd', 'e', 'f'})
