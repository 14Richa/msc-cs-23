# This is a useful data structure for implementing
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def get(self):
        return self.count


class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [set() for i in range(self.n)]

    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)

    # get a set of all vertices that
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]

    # Function: dfs_visit
    # Program a DFS visit of a graph.
    # We maintain a list of discovery times and finish times.
    # Initially all discovery times and finish times are set to None.
    # When a vertex is first visited, we will set discovery time
    # When DFS visit has processed all the neighbors then
    # set the finish time.
    # DFS visit should update the list of discovery and finish times in-place
    # Arguments
    #  i --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided for you.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node
    #                       if we visited node j from node i, then j's parent is i.
    #                      Do not forget to set tree_parent when you call dfs_visit
    #                                                         on node j from node i.
    #  dfs_back_edges --> a list of back edges.
    #                     a back edge is an edge from i to j wherein
    #                     DFS has already discovered j when i is discovered
    #                                     but not finished j

    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times,
                  dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] == None
        assert finish_times[i] == None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        # your code here
        # Sort
        sorted_neighbors = self.get_neighboring_vertices(i)
        for j in sorted_neighbors:
            # not visited
            if discovery_times[j] is None:
                dfs_tree_parent[j] = i
                self.dfs_visit(j, dfs_timer, discovery_times,
                               finish_times, dfs_tree_parent, dfs_back_edges)
            # it is not finished yet , back edge
            elif finish_times[j] == None:
                dfs_back_edges.append((i, j))

        finish_times[i] = dfs_timer.get()
        dfs_timer.increment()

    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None]*self.n
        finish_times = [None]*self.n
        dfs_tree_parents = [None]*self.n
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] == None:
                self.dfs_visit(i, dfs_timer, discovery_times, finish_times,
                               dfs_tree_parents, dfs_back_edges)
        # Clean up the back edges so that if (i,j) is a back edge then j cannot
        # be i's parent.
        non_trivial_back_edges = [(i, j) for (
            i, j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return (dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times)


def num_connected_components(g):
    dfs_timer = DFSTimeCounter()
    discovery_times = [None] * g.n
    dfs_tree_parents = [None] * g.n
    num_components = [0]  # Mutable list to store the number of components

    def dfs_visit(i):
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()

        for j in g.get_neighboring_vertices(i):
            if discovery_times[j] is None:
                dfs_tree_parents[j] = i
                dfs_visit(j)

        finish_times[i] = dfs_timer.get()
        dfs_timer.increment()

    finish_times = [None] * g.n

    for i in range(g.n):
        if discovery_times[i] is None:
            num_components[0] += 1
            dfs_visit(i)

    return num_components[0]


def find_all_nodes_in_cycle(g):
    set_of_nodes = set()
    # your code here

    parents, back_edges, _, _ = g.dfs_traverse_graph()

    for (backtrack_vertex, target_vertex) in back_edges:
        if parents[backtrack_vertex] != target_vertex:
            curr = backtrack_vertex
            while curr != target_vertex:
                set_of_nodes.add(curr)
                curr = parents[curr]
            set_of_nodes.add(target_vertex)
            set_of_nodes.add(backtrack_vertex)

    return set_of_nodes
