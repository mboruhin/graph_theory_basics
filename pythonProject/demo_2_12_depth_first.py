from demo_2_7_adjacency_matrix_and_2_9_adjacency_dict import *
from queue import Queue
import numpy as np


# --------------------------------------------------- Breadth First -------------------------------------------------- #
def action_breadth_first_for_connected(graph: Graph, start_vertex: int, action, *args, **kwargs):
    """ performs action on each node in breadth-first order.
        suitable for connected undirected graphs or strongly connected directed graphs """
    visited = np.zeros(graph.get_num_of_vertices())
    action_breadth_first_connected_sub_graph(graph, start_vertex, visited, action, *args, ** kwargs)


def action_breadth_first(graph: Graph, start_vertex: int, action, *args, **kwargs):
    """ performs action on each node in breadth-first order.
        suitable for connected and disconnected graphs """
    visited = np.zeros(graph.get_num_of_vertices())
    action_breadth_first_connected_sub_graph(graph, start_vertex, visited, action, *args, **kwargs)

    for vertex_id in range(graph.get_num_of_vertices()):
        action_breadth_first_connected_sub_graph(graph, vertex_id, visited, action, *args, **kwargs)


def action_breadth_first_connected_sub_graph(graph: Graph, start_vertex_id: int,
                                             visited: np.ndarray, action, *args, **kwargs):
    next_to_visit = Queue()
    next_to_visit.put(start_vertex_id)

    while not next_to_visit.empty():
        curr_vertex = next_to_visit.get()
        if visited[curr_vertex]:
            continue
        visited[curr_vertex] = 1
        action(curr_vertex, *args, **kwargs)

        for vertex in graph.get_adjacent_vertices(curr_vertex):
            if not visited[vertex]:
                next_to_visit.put(vertex)


# ----------------------------------------------------- Depth First -------------------------------------------------- #
def do_the_thing_depth_first(graph: Graph, start_vertex: int):
    pass

