# Class For Minheap
class MinHeap:

    # A minheap for a list of tuples, consisting of a key and a value
    def __init__(self, data_list):
        self.data_list = data_list
        self.build_min_heap_bottom_up()

    # Method to build min heap bottom up, using down-heapify
    def build_min_heap_bottom_up(self):
        # Starting from the first parent, we down-heapify
        for index in range(len(self.data_list) // 2, 0, -1):
            self.down_heapify(self.data_list, index)

    # Method to extract minimum, returns minimum and mutates the heap list
    def extract_min(self, heap_list):

        # Swapping the minimum with the last node in the heap and decreasing the list size
        minimum = heap_list[0]
        heap_list[0] = heap_list[-1]
        heap_list.pop()

        self.down_heapify(heap_list, 1)

        return minimum

    # Sorts this heap and returns the sorted list
    def heap_sort(self):

        sorted_list = []
        heap_list = self.data_list[:]

        # Sort by extracting the minimum repeatedly
        for i in range(len(heap_list)):
            sorted_list.append(self.extract_min(heap_list))

        return sorted_list

    # Method to down-heapify a node, using the node index (starting from one), mutates the list (based on the value of the tuples)
    def down_heapify(self, heap_list, node_index):
        size = len(heap_list)
        child_index = node_index * 2
        while child_index <= size:
            # Checking if both children exist
            if child_index + 1 <= size:
                # Seeing if the first child is less than the second one
                if heap_list[child_index - 1][1] < heap_list[child_index - 1 + 1][1]:
                    # Seeing if the chosen child is smaller than the parent
                    if heap_list[child_index - 1][1] < heap_list[node_index - 1][1]:
                        # swapping
                        tmp = heap_list[node_index - 1]
                        heap_list[node_index - 1] = heap_list[child_index - 1]
                        heap_list[child_index - 1] = tmp

                        # Updating index
                        node_index = child_index
                        child_index = node_index * 2

                    # If the chosen child is not smaller than parent
                    else:
                        return

                # The second child is chosen
                else:

                    # Seeing if the second child is smaller than parent
                    if heap_list[child_index - 1 + 1][1] < heap_list[node_index - 1][1]:
                        # swapping
                        tmp = heap_list[node_index - 1]
                        heap_list[node_index - 1] = heap_list[child_index - 1 + 1]
                        heap_list[child_index - 1 + 1] = tmp

                        # Updating index
                        node_index = child_index + 1
                        child_index = node_index * 2

                    # If the chosen child is not smaller than parent
                    else:
                        return

            # If only the first child exists
            elif child_index <= size:

                # Checking if it's smaller than its parent
                if heap_list[child_index - 1][1] < heap_list[node_index - 1][1]:
                    # swapping
                    tmp = heap_list[node_index - 1]
                    heap_list[node_index - 1] = heap_list[child_index - 1]
                    heap_list[child_index - 1] = tmp

                    # Updating index
                    node_index = child_index
                    child_index = node_index * 2

                # If the chosen child is not smaller than parent
                else:
                    return

            # If no child exists, we can terminate
            else:
                return
