import numpy as np
from abc import ABC, abstractmethod


class Graph(ABC):
    """ base class for graph classes. defines their interface """
    def __init__(self, num_of_vertices, is_directed: bool = True):
        self.num_of_vertices = num_of_vertices
        self.is_directed = is_directed

    @abstractmethod
    def add_edge(self, v1, v2, weight=1):
        pass

    @abstractmethod
    def get_adjacent_vertices(self, vertex):
        pass

    # @abstractmethod
    # def remove_edge(self, v1, v2):
    #     pass

    @abstractmethod
    def get_in_degree(self, vertex):
        # bla
        pass

    # @abstractmethod
    # def get_out_degree(self, vertex):
    #     pass

    @abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    # @abstractmethod
    def get_num_of_vertices(self):
        return self.num_of_vertices

    @abstractmethod
    def display(self):
        pass


# -------------------------------------------- AdjacencyMatrixGraph -------------------------------------------------- #

class AdjacencyMatrixGraph(Graph):
    """ base class for graph classes. defines their interface """
    def __init__(self, num_of_vertices: int, is_directed: bool = True):
        super(AdjacencyMatrixGraph, self).__init__(num_of_vertices, is_directed)
        self.matrix = np.zeros((num_of_vertices, num_of_vertices))

    def add_edge(self, v1, v2, weight=1):
        self._check_vertex(v1)
        self._check_vertex(v2)
        if v1 == v2:
            raise ValueError("can't create edge from vertex to itself")
        if weight < 1:
            raise ValueError("weight can't be smaller than 1")

        self.matrix[v1][v2] = weight
        if not self.is_directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, vertex):
        self._check_vertex(vertex)
        vertices = []
        j = 0
        while j < self.num_of_vertices:
            if self.matrix[vertex][j]:
                vertices.append(j)
            j += 1
        return vertices

    # def remove_edge(self, v1, v2):
    #     pass

    def get_in_degree(self, vertex):
        self._check_vertex(vertex)
        in_degree = 0
        i = 0
        while i < self.num_of_vertices:
            if self.matrix[i][vertex]:
                in_degree += 1
            i += 1
        return in_degree

    def get_out_degree(self, vertex):
        return len(self.get_adjacent_vertices(vertex))

    def get_edge_weight(self, v1, v2):
        self._check_vertex(v1)
        self._check_vertex(v2)
        return self.matrix[v1][v2]

    def _check_vertex(self, vertex):
        if vertex < 0 or vertex >= self.num_of_vertices:
            raise ValueError(f"vertex {vertex} is incorrect")

    def display(self):
        print(self.matrix)

    def display_with_arrows(self):
        arrow = " <-->"
        if self.is_directed:
            arrow = " --->"
        for i in range(self.num_of_vertices):
            row_to_print = str(i) + arrow
            for j in range(self.num_of_vertices):
                if self.matrix[i][j]:
                    row_to_print += " " + str(j)
            print(row_to_print)


    # def display_with_arrows(self):
    #     arrow = "<-->"
    #     if self.is_directed:
    #         arrow = "--->"
    #     for i in range(self.num_of_vertices):
    #         i_is_added = False
    #         row_to_print = ""
    #         for j in range(self.num_of_vertices):
    #             if self.matrix[i][j]:
    #                 if not i_is_added:
    #                     row_to_print += str(i) + arrow
    #                     i_is_added = True
    #                 row_to_print += " " + str(j)
    #         if i_is_added:
    #             print(row_to_print)


# ----------------------------------------------- AdjacencyListGraph ------------------------------------------------- #

class Vertex:
    """ holds id and a dict of  {adjacent vertex id, weight} """
    def __init__(self, vertex_id: int):
        self.vertex_id = vertex_id
        self.adjacency_dict = {}

    def add_edge(self, vertex_id: int, weight: int = 1):
        # if weight < 1:
        #     raise ValueError("weight of vertex must be greater than one")
        self.adjacency_dict[vertex_id] = weight

    def remove_edge(self, vertex_id: int):
        try:
            del self.adjacency_dict[vertex_id]
        except KeyError:
            raise ValueError(f"There is no edge between {self.vertex_id} and {vertex_id} to remove")

    def get_adjacent_vertices(self):
        return sorted(list(self.adjacency_dict.keys()))

    def get_out_degree(self):
        return len(self.adjacency_dict)

    def get_edge_weight(self, vertex):
        weight = None
        try:
            weight = self.adjacency_dict[vertex]
        except KeyError:
            pass
        return weight

    def __repr__(self):
        return f"vertex id: {self.vertex_id}"


class AdjacencyListGraph(Graph):
    """ base class for graph classes. defines their interface """
    def __init__(self, num_of_vertices: int, is_directed: bool = True):
        super(AdjacencyListGraph, self).__init__(num_of_vertices, is_directed)
        self._vertices = []
        for i in range(self.num_of_vertices):
            self._vertices.append(Vertex(i))

    def add_edge(self, v1, v2, weight=1):
        self._check_vertex(v1)
        self._check_vertex(v2)
        if v1 == v2:
            raise ValueError("can't create edge from vertex to itself")
        if weight < 1:
            raise ValueError("weight can't be smaller than 1")

        self._vertices[v1].add_edge(v2, weight)
        if not self.is_directed:
            self._vertices[v2].add_edge(v1, weight)

    def get_adjacent_vertices(self, vertex):
        self._check_vertex(vertex)
        return self._vertices[vertex].get_adjacent_vertices()

    def remove_edge(self, v1, v2):
        self._check_vertex(v1)
        self._check_vertex(v2)
        return self._vertices[v1].remove_edge(v2)

    def get_in_degree(self, vertex):
        self._check_vertex(vertex)
        in_degree = 0
        i = 0
        while i < self.num_of_vertices:
            if i != vertex:
                if vertex in self._vertices[i].get_adjacent_vertices():
                    in_degree += 1
            i += 1
        return in_degree

    def get_out_degree(self, vertex):
        return len(self.get_adjacent_vertices(vertex))

    def get_edge_weight(self, v1, v2):
        self._check_vertex(v1)
        self._check_vertex(v2)
        return self._vertices[v1].get_edge_weight(v2)

    def _check_vertex(self, vertex):
        if vertex < 0 or vertex >= self.num_of_vertices:
            raise ValueError(f"vertex {vertex} is incorrect")

    def display(self):
        arrow = "<-->"
        if self.is_directed:
            arrow = "--->"
        for i in range(self.num_of_vertices):
            print(i, arrow, ", ".join(str(num) for num in self.get_adjacent_vertices(i)))


# ----------------------------------------------------- Testing ------------------------------------------------------ #

def check_adjacency_matrix():
    print("AdjacencyMatrixGraph - directed:")
    g1 = AdjacencyMatrixGraph(5)
    g1.add_edge(0, 4)
    g1.add_edge(1, 2, 7)
    g1.add_edge(2, 3, 2)
    g1.add_edge(2, 4, 3)
    g1.add_edge(4, 2, 1)
    print("g1.get_adjacent_vertices(2) = ", g1.get_adjacent_vertices(2))
    g1.display()
    print("g1.get_out_degree(2) = ", g1.get_out_degree(2))
    print("g1.get_in_degree(2) = ", g1.get_in_degree(2))
    g1.display_with_arrows()

    print("-" * 30)
    print("undirected:")
    g2 = AdjacencyMatrixGraph(5, False)
    g2.add_edge(0, 4)
    g2.add_edge(1, 2, 7)
    g2.add_edge(2, 3, 2)
    g2.add_edge(2, 4, 3)
    g2.add_edge(4, 2, 1)
    print("g2.get_adjacent_vertices(2) = ", g2.get_adjacent_vertices(2))
    g2.display()
    print("g2.get_out_degree(2) = ", g2.get_out_degree(2))
    print("g2.get_in_degree(2) = ", g2.get_in_degree(2))
    g2.display_with_arrows()


def check_adjacency_list():
    print("check_adjacency_list - directed:")
    g1 = AdjacencyListGraph(5)
    g1.add_edge(0, 4)
    g1.add_edge(1, 2, 7)
    g1.add_edge(2, 3, 2)
    g1.add_edge(2, 4, 3)
    g1.add_edge(4, 2, 1)
    print("g1.get_adjacent_vertices(2) = ", g1.get_adjacent_vertices(2))
    g1.display()
    print("g1.get_out_degree(2) = ", g1.get_out_degree(2))
    print("g1.get_in_degree(2) = ", g1.get_in_degree(2))

    print("-" * 30)
    print("check_adjacency_list - undirected:")
    g2 = AdjacencyListGraph(5, False)
    g2.add_edge(0, 4)
    g2.add_edge(1, 2, 7)
    g2.add_edge(2, 3, 2)
    g2.add_edge(2, 4, 3)
    g2.add_edge(4, 2, 1)
    print("g2.get_adjacent_vertices(2) = ", g2.get_adjacent_vertices(2))
    g2.display()
    print("g2.get_out_degree(2) = ", g2.get_out_degree(2))
    print("g2.get_in_degree(2) = ", g2.get_in_degree(2))


def main():
    check_adjacency_matrix()
    print("\n" + 70*"-" + "\n")
    check_adjacency_list()


if __name__ == '__main__':
    main()
