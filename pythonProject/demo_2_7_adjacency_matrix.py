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
        pass

    # @abstractmethod
    # def get_out_degree(self, vertex):
    #     pass

    @abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

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
        arrow = "<-->"
        if self.is_directed:
            arrow = "--->"
        for i in range(self.num_of_vertices):
            i_is_added = False
            row_to_print = ""
            for j in range(self.num_of_vertices):
                if self.matrix[i][j]:
                    if not i_is_added:
                        row_to_print += str(i) + arrow
                        i_is_added = True
                    row_to_print += " " + str(j)
            if i_is_added:
                print(row_to_print)


def main():
    print("directed:")
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

    print("-" * 50)
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


if __name__ == '__main__':
    main()
