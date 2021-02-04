import numpy as np


class Graph:
    def __init__(self, numVertices, directed=False):
        if numVertices < 1:
            raise ValueError("graph must have at least one vertex")
        self.numVertices = numVertices
        self.directed = directed

    def add_edge(self, v1, v2, weight):
        pass

    def get_adjacent_vertices(self, v):
        pass

    def get_indegree(self, v):
        pass

    def get_edge_weight(self, v1, v2):
        pass

    def display(self):
        pass


# ################################################# AdjacencyMatrixGraph ###############################################


class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        self._sanity_check(v1)
        self._sanity_check(v2)
        if v1 == v2:
            raise ValueError("both vertices are the same")
        if weight < 1:
            raise ValueError("weight number is incorrect")

        self.matrix[v1][v2] = weight
        if self.directed is False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        self._sanity_check(v)
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] != 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        self._sanity_check(v)
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] != 0:
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display_matrix(self):
        print(self.matrix)

    def display(self):
        for v in range(self.numVertices):
            for v_a in range(self.numVertices):
                if self.matrix[v][v_a] != 0:
                    print(v, "-->", v_a)

    def _sanity_check(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("vertex number is incorrect")


# ################################################# AdjacencySetGraph ##################################################
# unweighted (all weights are 1)


class Vertex:
    """graph vertex for AdjacencySetGraph"""
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacent = set()

    def add_edge(self, v):
        if v == self.vertex_id:
            raise ValueError(f"the vertex {v} cant be adjacent to itself")
        self.adjacent.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacent)


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)
        self.vertices = []
        for i in range(self.numVertices):
            self.vertices.append(Vertex(i))

    def add_edge(self, v1, v2, weight=1):
        self._sanity_check(v1)
        self._sanity_check(v2)
        if v1 == v2:
            raise ValueError("both vertices are the same")
        if weight != 1:
            raise ValueError("only weight=1 is currently supported")
        self.vertices[v1].add_edge(v2)
        if self.directed is False:
            self.vertices[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        return self.vertices[v].get_adjacent_vertices()

    def get_indegree(self, v):
        count = 0
        for vertex in self.vertices:
            if vertex.vertex_id != v:
                if v in vertex.adjacent:
                    count += 1
        return count

    def get_edge_weight(self, v1, v2):
        return 1  # only weight=1 is currently supported

    def display(self):
        for v in self.vertices:
            print(v.vertex_id, "-->", sorted(v.adjacent))

    def _sanity_check(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("vertex number is incorrect")