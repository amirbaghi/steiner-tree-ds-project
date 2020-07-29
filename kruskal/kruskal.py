from data_structures.graph import Graph
from data_structures.union_find import UnionFind


# Class for Kruskal Algorithm
class Kruskal:

    # Static method for Kruskal algorithm, returns minimum spanning tree
    @staticmethod
    def kruskal_algorithm(graph):
        union_find = UnionFind(graph.number_of_nodes)
        sorted_edges_list = graph.sort_edges()
        mst_nodes = {}
        mst_edges = {}
        edge_number = 1
        for edge in sorted_edges_list:
            first_node = graph.edges[edge[0]][0]
            second_node = graph.edges[edge[0]][1]
            weight = edge[1]
            result = union_find.union(first_node - 1, second_node - 1)
            # The nodes were in different sets and union was successful, update the graph
            if result == 1:
                # Adding the nodes to the MST, also setting their terminal status
                mst_nodes[first_node] = graph.nodes[first_node][1]
                mst_nodes[second_node] = graph.nodes[second_node][1]

                # Adding the edge to the MST
                mst_edges[edge_number] = [first_node, second_node, weight]
                edge_number += 1

        minimum_spanning_tree = Graph(len(mst_nodes), len(mst_edges), mst_nodes, mst_edges)
        return minimum_spanning_tree, minimum_spanning_tree.graph_weight()
