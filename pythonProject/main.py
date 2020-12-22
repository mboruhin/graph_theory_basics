from graph import *

g = AdjacencyMatrixGraph(5, True)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(1, 0)
g.add_edge(1, 4)
g.add_edge(2, 0)
g.add_edge(2, 4)
g.add_edge(4, 3, 8)
g.display()
g.display_matrix()
list0 = g.get_adjacent_vertices(0)
list1 = g.get_adjacent_vertices(1)
list4 = g.get_adjacent_vertices(4)
print("list0:", list0)
print("list1:", list1)
print("list4:", list4)
print("g.get_indegree(0):", g.get_indegree(0))
print("g.get_indegree(1):", g.get_indegree(1))
print("g.get_indegree(4):", g.get_indegree(4))

print("g.get_edge_weight(4, 0):", g.get_edge_weight(4, 3))

# ################################### AdjacencySetGraph ############################################
g2 = AdjacencySetGraph(5, True)
g2.add_edge(0, 4)
g2.add_edge(1, 0)
g2.add_edge(1, 3)
g2.add_edge(1, 4)
g2.add_edge(2, 0)
g2.add_edge(2, 4)
g2.add_edge(4, 3)
print("g2.get_adjacent_vertices(1):", g2.get_adjacent_vertices(1))
g2.display()
print("g2.get_indegree(0):", g2.get_indegree(0))
print("g2.get_indegree(1):", g2.get_indegree(1))
print("g2.get_indegree(2):", g2.get_indegree(2))
print("g2.get_indegree(3):", g2.get_indegree(3))
print("g2.get_indegree(4):", g2.get_indegree(4))