import sys
sys.path.append('../graph')
from util import Stack

# Create a graph class
# dictionary of vertices, values are lists of 2 sets
#       list[0] is parents, list[1] is children
class Anc_Graph():
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        parents = set()
        children = set()
        self.vertices[vertex_id] = [parents, children]
        
    def add_edge(self, parent, child):
        if parent in self.vertices and child in self.vertices:

            self.vertices[child][0].add(parent)
            self.vertices[parent][1].add(child)
        elif child in self.vertices:
            self.add_vertex(parent)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
        elif parent in self.vertices:
            self.add_vertex(child)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
        else:
            self.add_vertex(parent)
            self.add_vertex(child)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
    
    def get_parents(self, v):
        return self.vertices[v][0]

def earliest_ancestor(ancestors, starting_node):
    anc_tree = Anc_Graph()
    # fill graph
    for i in range(len(ancestors)):
        anc_tree.add_edge(ancestors[i][0], ancestors[i][1])

    # account for no ancestors
    if anc_tree.get_parents(starting_node) == set():
        return -1
    # create visited set to keep track of visited nodes
    visited = set()
    # longest_paths to keep track of longest paths, and longest paths of same length
    longest_paths = [[starting_node]]
    
    s = Stack()
    s.push([starting_node])
    while s.size() > 0:
        new_path = s.pop()
        last_node = new_path[-1]
        if last_node not in visited:
            visited.add(last_node)
            if len(new_path) > len(longest_paths[0]):
                longest_paths = [new_path]
    
            elif len(new_path) == len(longest_paths[0]):
                longest_paths.append(new_path)
            for parent in anc_tree.get_parents(last_node):
                path_copy = new_path.copy()
                if parent is not set():
                    path_copy.append(parent)
                    s.push(path_copy)
    # check for duplicate longest paths
    if len(longest_paths) > 1:
        low_id = float('inf')
        for i in range(len(longest_paths)):
            if longest_paths[i][-1] < low_id:
                low_id = longest_paths[i][-1]
        print(starting_node, low_id)
        return low_id
    # if no duplicates, return the last index of longest path
    print(starting_node, longest_paths[0][-1])
    return longest_paths[0][-1]

    # print(anc_tree.vertices)

# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9))