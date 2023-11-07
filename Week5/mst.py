class DisjointForests:
    def __init__(self, n):
        assert n >= 1, ' Empty disjoint forest is disallowed'
        self.n = n
        self.parents = [None]*n
        self.rank = [None]*n

    # Function: dictionary_of_sets
    # Convert the disjoint forest structure into a dictionary d
    # wherein d has an entry for each representative i
    # d[i] maps to each elements which belongs to the tree corresponding to i
    # in the disjoint forest.
    def dictionary_of_sets(self):
        d = {}
        for i in range(self.n):
            if self.is_representative(i):
                d[i] = set([i])
        for j in range(self.n):
            if self.parents[j] != None:
                root = self.find(j)
                assert root in d
                d[root].add(j)
        return d

    def make_set(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] == None, 'You are calling make_set on an element multiple times -- not allowed.'
        self.parents[j] = j
        self.rank[j] = 1

    def is_representative(self, j):
        return self.parents[j] == j

    def get_rank(self, j):
        return self.rank[j]

    # Function: find
    # Implement the find algorithm for a node j in the set.
    # Repeatedly traverse the parent pointer until we reach a root.
    def find(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] != None, 'You are calling find on an element that is not part of the family yet. Please call make_set first.'
        # your code here
        if self.parents[j] != j:
            # Set the parent to the representative of the set
            self.parents[j] = self.find(self.parents[j])
        return self.parents[j]


    # Function : union
    # Compute union of j1 and j2
    # First do a find to get to the representatives of j1 and j2.
    # If they are not the same, then
    #  implement union using the rank strategy I.e, lower rank root becomes
    #  child of the higher ranked root.
    #  break ties by making the first argument j1's root the parent.
    def union(self, j1, j2):
        assert 0 <= j1 < self.n
        assert 0 <= j2 < self.n
        assert self.parents[j1] != None
        assert self.parents[j2] != None
        # your code here

        root1 = self.find(j1)
        root2 = self.find(j2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parents[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2
                self.rank[root2] += 1

def compute_mst(g):
    # return a tuple of two items
    #   1. list of edges (i,j) that are part of the MST
    #   2. sum of MST edge weights.
    d = DisjointForests(g.n)
    mst_edges = []
    g.sort_edges()
    # your code here
    d = DisjointForests(g.n)

    for i in range(g.n):
        d.make_set(i)

    mst_edges = []
    mst_weight = 0

    edges = g.sort_edges()

    for edge in edges:
        i, j, wij = edge
        # Check if adding this edge creates a cycle
        if d.find(i) != d.find(j):
            # Add edge to the MST
            mst_edges.append((i, j, wij))
            mst_weight += wij
            # Union the vertices to avoid cycles
            d.union(i, j)

    return mst_edges, mst_weight

class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # We simply store the edges in a list.
    def __init__(self, n):
        assert n >= 1, 'You are creating an empty graph -- disallowed'
        self.n = n
        self.edges = []
        self.vertex_data = [None]*self.n


    def set_vertex_data(self, j, dat):
        assert 0 <= j < self.n
        self.vertex_data[j] = dat

    def get_vertex_data(self, j):
        assert 0 <= j < self.n
        return self.vertex_data[j]

    def add_edge(self, i, j, wij):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j with weight wij
        self.edges.append((i, j, wij))

    def sort_edges(self):
        # sort edges in ascending order of weights.
        self.edges = sorted(self.edges, key=lambda edg_data: edg_data[2])
        return self.edges