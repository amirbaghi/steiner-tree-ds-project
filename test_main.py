from data_structures.graph import Graph
from data_structures.minheap import MinHeap
from data_structures.union_find import UnionFind
from file_handling.file_handler import FileHandler
from kruskal.kruskal import Kruskal


def test_minheap_down_heapify():
    data_list = [(5, 5), (6, 6), (4, 4), (12, 12), (1, 1), (2, 2)]
    min_heap = MinHeap(data_list)
    sorted_list = min_heap.heap_sort()
    print(sorted_list)
    print(min_heap.data_list)


def test_union_find():
    union_find = UnionFind(7)
    union_find.union(0, 1)
    union_find.union(1, 6)
    union_find.union(2, 3)
    union_find.union(6, 3)
    union_find.union(3, 5)
    print([x.size for x in union_find.sets])
    print(union_find.parent)


def test_graph():
    terminals = [1, 4]
    nodes = [1, 2, 3, 4]
    edges = {1: [1, 3, 2], 2: [3, 2, 4], 3: [1, 4, 1], 4: [2, 4, 5]}
    graph = Graph(4, 4, {k: 1 if k in terminals else 0 for k in nodes},
                  {1: [1, 3, 2], 2: [3, 2, 4], 3: [1, 4, 1], 4: [2, 4, 5]})
    print(graph.nodes)
    print(graph.edges)
    print(graph.sort_edges())


def read_file_test():
    comment, graph, terminals = FileHandler.read_stp_file(
        "/home/amir/Desktop/dev/steiner-tree-ds/steiner-tree-ds-project/inputs/bip42p.stp")
    print(comment)
    print(graph)
    print(terminals)


def test_file_data_to_graph():
    comment, graph, terminals = FileHandler.read_stp_file(
        "/home/amir/Desktop/dev/steiner-tree-ds/steiner-tree-ds-project/inputs/bip42p.stp")
    terminal_nodes = [terminals[k] for k in range(1, terminals['Terminals'] + 1)]
    graph = Graph(graph['Nodes'], graph['Edges'],
                  {k: 1 if k in terminal_nodes else 0 for k in range(1, graph['Nodes'] + 1)},
                  {k: graph[k] for k in range(1, graph['Edges'] + 1)}
                  )
    print(graph.nodes)
    print(graph.edges)
    print(graph.sort_edges())


def test_kruskal():
    terminals = [2, 5, 7]
    nodes = [i for i in range(1, 8)]
    graph = Graph(7, 9, {k: 1 if k in terminals else 0 for k in nodes},
                  {1: [1, 2, 28], 2: [2, 3, 16], 3: [3, 4, 12], 4: [4, 5, 22], 5: [5, 6, 25], 6: [6, 1, 10],
                   7: [2, 7, 14],
                   8: [7, 5, 24], 9: [7, 4, 18]})
    mst = Kruskal.kruskal_algorithm(graph)
    print(mst[0].find_non_terminal_leaves())
    print(mst[1])
    return mst


def test_kruskal_on_stp_file():
    comment, graph, terminals = FileHandler.read_stp_file(
        "/home/amir/Desktop/dev/steiner-tree-ds/steiner-tree-ds-project/inputs/bip42p.stp")
    terminal_nodes = [terminals[k] for k in range(1, terminals['Terminals'] + 1)]
    graph = Graph(graph['Nodes'], graph['Edges'],
                  {k: 1 if k in terminal_nodes else 0 for k in range(1, graph['Nodes'] + 1)},
                  {k: graph[k] for k in range(1, graph['Edges'] + 1)}
                  )
    mst = Kruskal.kruskal_algorithm(graph)
    print(mst[0].find_non_terminal_leaves())
    print(mst[1])
    return mst


# test_minheap_down_heapify()
# test_union_find()
# read_file_test()
# test_graph()
# test_file_data_to_graph()
# test_kruskal()
test_kruskal_on_stp_file()
