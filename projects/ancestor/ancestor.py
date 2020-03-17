# class Gr_Node():
#     def __init__(self, value):
#         self.value = value
#         self.parents = set()
#         self.children = set()


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
        
my_gr = Anc_Graph()

my_gr.add_vertex(75)
my_gr.add_child(75, 32)
my_gr.add_child(32, 1)
my_gr.add_child(32, 2)
my_gr.add_child(100, 75)
print(my_gr.vertices)
# seems to be single direction, parents to children??
# store parent node, with a set/list of children nodes?
# adding nodes requires 2 args, (parent, child)
# parents can share children
def earliest_ancestor(ancestors, starting_node):
    pass