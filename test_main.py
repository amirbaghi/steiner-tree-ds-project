from data_structures.minheap import MinHeap
from data_structures.union_find import UnionFind
from file_handling.file_handler import FileHandler


def test_minheap_down_heapify():
    data_list = [5, 6, 4, 12, 1, 2]
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



def read_file_test():
    comment, graph, terminals = FileHandler.read_stp_file(
        "/home/amir/Desktop/dev/steiner-tree-ds/steiner-tree-ds-project/inputs/bip42p.stp")
    print(comment)
    print(graph)
    print(terminals)


test_union_find()