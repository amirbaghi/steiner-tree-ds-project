# Union-Find Data Structure (With Path-Compression)
class UnionFind:

    def __init__(self, number_of_sets):
        # The Set List
        self.sets = [Set(i, 1) for i in range(number_of_sets)]
        # Parent Index List
        self.parent = [i for i in range(number_of_sets)]

    # Find Root (With Path-Compression Scheme)
    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Union Two Sets, returns 0 if they were in the same set, returns 1 otherwise
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        # Checking if they're in the same set
        if x_parent == y_parent:
            return 0

        # Not in the Same Set, with different size scenarios
        if self.sets[x_parent].size < self.sets[y_parent].size:
            self.parent[x_parent] = y_parent
            self.sets[y_parent].size += 1

        else:
            self.parent[y_parent] = x_parent
            self.sets[x_parent].size += 1

        return 1


# Class for a Set
class Set:

    def __init__(self, root, size):
        self.root = root
        self.size = size
