from demo_2_7_adjacency_matrix_and_2_9_adjacency_dict import *
from queue import Queue


def do_the_thing_breadth_first(graph: Graph, start_vertex: int, the_thing, *args, **kwargs):
    next_to_visit = Queue()
    next_to_visit.put(start_vertex)
    visited = set()

    while not next_to_visit.empty():
        curr_vertex = next_to_visit.get()
        if curr_vertex in visited:
            continue


def do_the_thing_depth_first(graph: Graph, start_vertex: int):
    pass


def thing_test_print(node):
    print(node)
