# Graph Class
from data_structures.minheap import MinHeap


class Graph:

    def __init__(self, number_of_nodes, number_of_edges, edges, terminals):
        self.number_of_nodes = number_of_nodes
        self.number_of_edges = number_of_edges
        # Edges are a list, with indexes 0, 1, and 2 being first and second node and the weight respectively
        self.edges = edges
        self.terminals = terminals
        # A dictionary with keys being the node number and the values being 1 if it's a terminal or 0 if it's not
        self.nodes = {(k, 1 if k in terminals else 0) for k in range(1, number_of_nodes + 1)}

    # Sorting edges using Heap-Sort, returns a list consisting of a key (edge index) and value (its weight)
    def sort_edges(self):
        edges = [(k, self.edges[k][2]) for k in range(1, self.number_of_edges + 1)]
        min_heap = MinHeap(edges)
        sorted_edges = min_heap.heap_sort()
        return sorted_edges
