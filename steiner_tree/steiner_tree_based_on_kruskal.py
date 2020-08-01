# Class for Solving the Steiner Tree problem based on Kruskal
from data_structures.graph import Graph


class SteinerTreeBasedOnKruskal:

    # Method to return the Steiner Tree for an MST
    @staticmethod
    def steiner_tree(graph):
        leaf_nodes = graph.find_non_terminal_leaves()
        # Get a copy of the graph edges
        # we are going to delete edges from this dictionary (by setting their value to an empty list)
        new_edges = graph.edges.copy()
        # Same with the nodes
        new_nodes = graph.nodes.copy()
        # For all non-terminal leaves in the MST
        for leaf in leaf_nodes:
            node_num = leaf[0]
            edge_num = leaf[1][0]
            leaf_edge = graph.edges[edge_num]
            # Second node connected to the edge
            second_node = leaf_edge[0] if leaf_edge[1] == node_num else leaf_edge[1]
            # Setting the value of the chosen edge and node to [] (as if we have delete it)
            new_edges[edge_num] = []
            new_nodes[node_num] = []

            last_deleted_edge = edge_num
            # Checking if the remaining node is a leaf and not a terminal
            while graph.nodes[second_node][2] == 0 and len(graph.nodes[second_node][1]) == 2:
                node_num = second_node
                node_edges = graph.nodes[second_node][1]
                edge_num = node_edges[0] if node_edges[1] == last_deleted_edge else node_edges[1]
                leaf_edge = graph.edges[edge_num]

                second_node = leaf_edge[0] if leaf_edge[1] == node_num else leaf_edge[1]

                new_edges[edge_num] = []
                new_nodes[node_num] = []

                last_deleted_edge = edge_num

        # Making new dictionaries of the updated nodes and edges to make a graph from them
        new_graph_nodes = {k: v[2] for k, v in new_nodes.items() if v != []}
        edge_number = 1
        new_graph_edges = {}
        for k, v in new_edges.items():
            if v:
                new_graph_edges[edge_number] = v
                edge_number += 1

        steiner_tree = Graph(len(new_graph_nodes), len(new_graph_edges), new_graph_nodes, new_graph_edges)

        return steiner_tree, steiner_tree.graph_weight()
