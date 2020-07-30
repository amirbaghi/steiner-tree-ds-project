# Graph Class
from functools import reduce

from data_structures.minheap import MinHeap


class Graph:

    def __init__(self, number_of_nodes, number_of_edges, nodes, edges):
        self.number_of_nodes = number_of_nodes
        self.number_of_edges = number_of_edges
        # Edges are a list, with indexes 0, 1, and 2 being first and second node and the weight respectively
        self.edges = edges
        # Finding the Degree and the edges of each node
        node_degrees = {k: [0, []] for k in list(nodes.keys())}
        for i, edge in enumerate(list(self.edges.values())):
            node_degrees[edge[0]][0] += 1
            node_degrees[edge[0]][1].append(i + 1)
            node_degrees[edge[1]][0] += 1
            node_degrees[edge[1]][1].append(i + 1)

        # A dictionary with keys being the node number and the values being a list including the node degree (index 0),
        # the edges (index 1), and 1 if it's terminal or 0 if it's not (index 2)
        self.nodes = {k: [node_degrees[k][0], node_degrees[k][1], nodes[k]] for k in list(nodes.keys())}
        # self.nodes = {k: 1 if k in terminals else 0 for k in nodes}

    # Sorting edges using Heap-Sort, returns a list consisting of a key (edge index) and value (its weight)
    def sort_edges(self):
        edges = [(k, self.edges[k][2]) for k in range(1, self.number_of_edges + 1)]
        min_heap = MinHeap(edges)
        sorted_edges = min_heap.heap_sort()
        return sorted_edges

    # Method to return total weight of Graph
    def graph_weight(self):
        current_sum = 0
        edges = list(self.edges.values())
        for edge in edges:
            current_sum += edge[2]
        return current_sum

    # Find leaf Nodes in the Tree that are not terminal
    def find_non_terminal_leaves(self):
        leaves = [(k, v[1]) for k, v in self.nodes.items() if v[0] == 1 and v[2] != 1]
        return leaves
