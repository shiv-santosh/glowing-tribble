import sys


class MinSpanningTree:

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

        print(mst)
        return mst

    @staticmethod
    def find_minimum_edge_vertex(graph, mst_v):
        min_edge_weight = sys.maxsize
        mev = None
        for fv in mst_v:
            if graph.get(fv) is None:
                print(fv)
                print(graph)
            for tv, e in graph.get(fv).items():
                if tv in mst_v:
                    continue
                if e < min_edge_weight:
                    mev = (fv, tv)
                    min_edge_weight = e
        return mev


# undirected graph
def add_edge(graph, from_v, to_v, weight):
    if from_v not in graph:
        graph[from_v] = {
            to_v: weight
        }
    else:
        graph[from_v][to_v] = weight

    if to_v not in graph:
        graph[to_v] = {
            from_v: weight
        }
    else:
        graph[to_v][from_v] = weight


if __name__ == '__main__':
    graph = {}
    add_edge(graph, 'a', 'b', 3)
    add_edge(graph, 'a', 'f', 5)
    add_edge(graph, 'a', 'e', 6)

    add_edge(graph, 'b', 'f', 4)
    add_edge(graph, 'b', 'c', 1)

    add_edge(graph, 'f', 'c', 4)
    add_edge(graph, 'f', 'd', 5)
    add_edge(graph, 'f', 'e', 2)

    add_edge(graph, 'c', 'd', 6)

    add_edge(graph, 'd', 'e', 8)

    # for i,v in graph.items():
    #     print(i, v)
    MinSpanningTree.prims(graph, {'a', 'b', 'c', 'd', 'e', 'f'})
