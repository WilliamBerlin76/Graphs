import sys
sys.path.append('../graph')
from util import Stack

# Create a graph and node class
# dictionary of vertices, values are lists of 2 sets
#       list[0] is parents, list[1] is children
class Anc_Graph():
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        parents = set()
        children = set()
        self.vertices[vertex_id] = [parents, children]
        
    def add_child(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v2][0].add(v1)
            self.vertices[v1][1].add(v2)
        elif v2 in self.vertices:
            self.add_vertex(v1)
            self.vertices[v1][1].add(v2)
            self.vertices[v2][0].add(v1)
        elif v1 in self.vertices:
            self.add_vertex(v2)
            self.vertices[v1][1].add(v2)
            self.vertices[v2][0].add(v1)
        else:
            self.add_vertex(v1)
            self.add_vertex(v2)
            self.vertices[v1][1].add(v2)
            self.vertices[v2][0].add(v1)
    
    def add_parent(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2][1].add(v1)
            self.vertices[v1][0].add(v2)
        elif v2 in self.vertices:
            self.add_vertex(v1)
            self.vertices[v1][0].add(v2)
            self.vertices[v2][1].add(v1)
        elif v1 in self.vertices:
            self.add_vertex(v2)
            self.vertices[v1][0].add(v2)
            self.vertices[v2][1].add(v1)
        else:
            self.add_vertex(v1)
            self.add_vertex(v2)
            self.vertices[v1][0].add(v2)
            self.vertices[v2][1].add(v1)
    def get_parents(self, v):
        return self.vertices[v][0]
# my_gr = Anc_Graph()

# my_gr.add_vertex(75)
# my_gr.add_child(75, 32)
# my_gr.add_child(32, 1)
# my_gr.add_child(32, 2)
# my_gr.add_child(100, 75)
# my_gr.add_parent(32, 88)
# my_gr.add_parent(75, 88)
# print(my_gr.vertices)


# parents can share children
def earliest_ancestor(ancestors, starting_node):
    anc_tree = Anc_Graph()
    # fill graph
    for i in range(len(ancestors)):
        anc_tree.add_child(ancestors[i][0], ancestors[i][1])

    # account for no ancestors
    if anc_tree.get_parents(starting_node) == set():
        return -1
    # create visited set
    visited = set()
    # longest_path to keep track of path
    longest_path = [starting_node]
    # dup_paths to account for duplicate seperate longest paths
    dup_paths = [[longest_path]]
    # count to keep track of the longest path
    # longest_path_len = len(longest_path)
    s = Stack()
    s.push([starting_node])
    while s.size() > 0:
        new_path = s.pop()
        last_node = new_path[-1]
        if last_node not in visited:
            visited.add(last_node)
            if len(new_path) > len(longest_path):
                longest_path = new_path
                dup_paths = [longest_path]
            elif len(new_path) == len(longest_path):
                dup_paths.append(new_path)
            for parent in anc_tree.get_parents(last_node):
                path_copy = new_path.copy()
                if parent is not set():
                    path_copy.append(parent)
                    s.push(path_copy)
    # check for duplicate max paths
    if len(dup_paths) > 1:
        low_id = float('inf')
        for i in range(len(dup_paths)):
            if dup_paths[i][-1] < low_id:
                low_id = dup_paths[i][-1]
        return low_id
    # if no duplicates, return the last index of longest path
    return longest_path[-1]

    # print(anc_tree.vertices)

# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9))