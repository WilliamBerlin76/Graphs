"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("ERROR: vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visitied
                print(v)
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
                

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # Check if it's been visited
            if v not in visited:
            # If it hasn't been visited...
                print(v)
                # Mark it as visitied
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create visited set to store visited vertices
        visited = set()
        # Create nested recursive helper function
        def recurse_helper(starting_vertex):
            # Check if the node has been visited
            if starting_vertex not in visited:
            # If not...
                print(starting_vertex)
                # Mark it as visited
                visited.add(starting_vertex)
                # Call helper function on each neighbor
                for neighbor in self.get_neighbors(starting_vertex):
                    recurse_helper(neighbor)
        # Call the helper function
        recurse_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            last_vert = path[-1]
            # Check if it's been visited
            if last_vert not in visited:
            # If it hasn't been visited...
                # print(last_vert)
                # Mark it as visited
                visited.add(last_vert)
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    print(path)
                    return path
                    # IF SO, RETURN THE PATH
                # Enqueue A PATH TO all it's neighbors
                
                for neighbor in self.get_neighbors(last_vert):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    # ENQUEUE THE COPY
                    path_copy.append(neighbor)
                    if neighbor is destination_vertex:
                        print(path_copy)
                        return path_copy
                    
                    q.enqueue(path_copy)
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            path = s.pop()
            last_vert = path[-1]
            if last_vert not in visited:
                visited.add(last_vert)
                if last_vert == destination_vertex:
                    print(path)
                    return path
                
                for neighbor in self.get_neighbors(last_vert):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    if neighbor is destination_vertex:
                        print(path_copy)
                        return path_copy
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        init_path = [starting_vertex]
        def recurse_helper(path):
            v = path[-1]
            if v is destination_vertex:
                # path.append(vertex)
                print(path)
                return path
            if v not in visited:
                visited.add(v)
                
                if v == destination_vertex:
                    return path
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    if neighbor is destination_vertex:
                        print(path_copy)
                        return path_copy
                    new_path = recurse_helper(path_copy)
                    if new_path is not None:
                        return new_path

                        
        return recurse_helper(init_path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print('START BFS')
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print('START DFS')
    print(graph.dfs(1, 6))
    print('START DFS RECURSIVE')
    print(graph.dfs_recursive(1, 6))
