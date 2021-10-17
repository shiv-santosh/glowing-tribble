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


class Solution:

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

    class DistanceMapHelper:

        def __init__(self, graph, vertices, starting_vertex):
            self.distance_map = self.get_init_distance_map(graph, vertices, starting_vertex)
            self.selected_vertices = {starting_vertex}
            self.vertices = vertices

        @staticmethod
        def get_init_distance_map(graph, vertices, starting_vertex):
            distance_map = {}
            starting_vertex_edges = graph.get(starting_vertex, {})
            for vertex in vertices:
                if vertex == starting_vertex:
                    continue
                distance_map[vertex] = starting_vertex_edges.get(vertex, float('inf'))
            return distance_map

        def process_vertex(self, vertex):
            self.selected_vertices.add(vertex)

        def has_unprocessed_vertices(self):
            return self.selected_vertices != self.vertices

        def get_next_vertex(self):
            min_vertex = None
            min_weight = None
            for vertex, weigth in self.distance_map.items():
                if self.is_vertex_processed(vertex):
                    continue
                if min_weight is None or weigth < min_weight:
                    min_weight = weigth
                    min_vertex = vertex
            self.process_vertex(min_vertex)
            return min_vertex

        def is_vertex_processed(self, vertex):
            return vertex in self.selected_vertices

        def update(self, vertex, weight):
             self.distance_map[vertex] = weight

        def get_current_weight(self, vertex):
            return self.distance_map[vertex]

        def __str__(self):
            s = ''
            for to_v, weight in self.distance_map.items():
                s += str(to_v) + ": " + str(weight) + '\n'
            return s

    class DistanceMapHelperOpt:

        distance_map = {}

        def __init__(self, graph, vertices, starting_vertex):
            self.map_heap = MapHeap(self.get_init_distance_list(graph, vertices, starting_vertex))
            self.distance_map = self.get_init_distance_map(graph, vertices, starting_vertex)
            self.selected_vertices = {starting_vertex}
            self.vertices = vertices

        @staticmethod
        def get_init_distance_map(graph, vertices, starting_vertex):
            distance_map = {}
            starting_vertex_edges = graph.get(starting_vertex, {})
            for vertex in vertices:
                if vertex == starting_vertex:
                    continue
                distance_map[vertex] = starting_vertex_edges.get(vertex, float('inf'))
            return distance_map

        @staticmethod
        def get_init_distance_list(graph, vertices, starting_vertex):
            distance_list = []
            starting_vertex_edges = graph.get(starting_vertex, {})
            for vertex in vertices:
                if vertex == starting_vertex:
                    continue
                distance_list.append([vertex, starting_vertex_edges.get(vertex, float('inf'))])
            return distance_list

        def has_unprocessed_vertices(self):
            return not self.map_heap.is_empty()

        def get_next_vertex(self):
            return self.map_heap.extract_min()

        def update(self, vertex, weight):
            self.distance_map[vertex] = weight
            self.map_heap.update(vertex, weight)

        def is_vertex_processed(self, vertex):
            return not self.map_heap.contains(vertex)

        def get_current_weight(self, vertex):
            return self.map_heap.heap[self.map_heap.mapping[vertex]][1]

        def __str__(self):
            s = ''
            for to_v, weight in self.distance_map.items():
                s += str(to_v) + ": " + str(weight) + '\n'
            return s

    # Directed
    @staticmethod
    def add_edge(graph, edge: Edge):
        if edge.from_v not in graph:
            graph[edge.from_v] = {
                edge.to_v: edge.val
            }
        else:
            graph[edge.from_v][edge.to_v] = edge.val

    def djikstras(self, graph, vertices, starting_vertex):
        distance_map_helper = Solution.DistanceMapHelper(graph, vertices, starting_vertex)

        # while unprocessed vertex
        while distance_map_helper.has_unprocessed_vertices():
            next_vertex = distance_map_helper.get_next_vertex()
            # for all edges from the next min edge to unprocessed vertices
            for to_vertex, weight in graph.get(next_vertex, {}).items():
                if distance_map_helper.is_vertex_processed(to_vertex):
                    continue
                # relax if applicable
                distance_through_cur_min = graph.get(next_vertex, {}).get(to_vertex, float('inf')) + distance_map_helper.get_current_weight(next_vertex)
                if distance_through_cur_min < distance_map_helper.get_current_weight(to_vertex):
                    distance_map_helper.update(to_vertex, distance_through_cur_min)
        print(distance_map_helper)
        return distance_map_helper

    def djikstrasOpt(self, graph, vertices, starting_vertex):
        distance_map_helper = Solution.DistanceMapHelperOpt(graph, vertices, starting_vertex)

        # while unprocessed vertex
        while distance_map_helper.has_unprocessed_vertices():
            next_vertex, current_weight = distance_map_helper.get_next_vertex()
            # for all edges from the next min edge to unprocessed vertices
            for to_vertex, weight in graph.get(next_vertex, {}).items():
                if distance_map_helper.is_vertex_processed(to_vertex):
                    continue
                # relax if applicable
                distance_through_cur_min = graph.get(next_vertex, {}).get(to_vertex, float('inf')) + current_weight
                if distance_through_cur_min < distance_map_helper.get_current_weight(to_vertex):
                    distance_map_helper.update(to_vertex, distance_through_cur_min)
        print(distance_map_helper)
        return distance_map_helper


if __name__ == '__main__':
    graph = {}
    s = Solution()
    s.add_edge(graph, Solution.Edge(1, 2, 50))
    s.add_edge(graph, Solution.Edge(1, 3, 45))
    s.add_edge(graph, Solution.Edge(1, 4, 10))
    s.add_edge(graph, Solution.Edge(2, 3, 10))
    s.add_edge(graph, Solution.Edge(2, 4, 15))
    s.add_edge(graph, Solution.Edge(3, 5, 30))
    s.add_edge(graph, Solution.Edge(4, 1, 15))
    s.add_edge(graph, Solution.Edge(4, 5, 15))
    s.add_edge(graph, Solution.Edge(5, 2, 20))
    s.add_edge(graph, Solution.Edge(5, 3, 35))
    s.add_edge(graph, Solution.Edge(6, 5, 3))
    s.djikstrasOpt(graph, set(range(1, 7)), 1)
