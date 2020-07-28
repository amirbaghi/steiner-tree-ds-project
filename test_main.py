from data_structures.minheap import MinHeap


def test_minheap_down_heapify():
    data_list = [5, 6, 4, 12, 1, 2]
    min_heap = MinHeap(data_list)
    sorted_list = min_heap.heap_sort()
    print(sorted_list)
    print(min_heap.data_list)

test_minheap_down_heapify()
