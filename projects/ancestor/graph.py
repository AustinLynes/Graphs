"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import random
import sys 
sys.setrecursionlimit(10**6) 

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    """
    Add a vertex to the graph.
    """
    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices:
            return 
        
        self.vertices[vertex_id] = set()
    
    def get_vertices(self):
        return self.vertices

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            return

        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            return 

        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        USES QUEUE
        """
        # path = ""
        if starting_vertex not in self.vertices:
            return 
        q = Queue()
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while the Queue has something to do
        while q.size() > 0:
            current_node = q.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)

                neighbors = self.get_neighbors(current_node)
                for n in neighbors:
                    q.enqueue(n)

   

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        USES STACK
        """
        # create a stack to handle depth-first-traversal
        s = Stack()
        # add the starting vertex to the stack
        s.push(starting_vertex)
        # create a set to track the visited nodes
        visitied = set()

        # if the stack has something to do...
        while s.size() > 0:
            # grab the current node from the stack
            cur_node = s.pop()
            # check the current node to see if it has been visited....
            if cur_node not in visitied:
                # if it hasent.. then add it to the visited set
                visitied.add(cur_node)
                # print the current node we are loooking at 
                print(cur_node)
                # grab the neighbors from the current node
                neighbors = self.get_neighbors(cur_node)
                # iterate over the neighbors
                for n in neighbors:
                    # add the current neighbor to the stack 
                    s.push(n)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
            
        # check if we have been visited
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
        # base case: if no neighbors
            neighbors = self.get_neighbors(starting_vertex)
            if len(neighbors) == 0:
                return visited
        # if we do have neighbors... iterate over them and recurse for each one 
            for n in neighbors:
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # path = ""
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            return 
        
        q = Queue()


        # make a to track visited nodes
        visited = set()
        path = [starting_vertex]
        q.enqueue(path)

        # while the Queue has something to do
        while q.size() > 0:
            # take the current node from the queue
            cur_path = q.dequeue()
            # grab the current note from the current path we are looking at
            cur_node = cur_path[-1]
            # check to see if this is the node we are looking for
            if cur_node == destination_vertex:
                # return it because the current path is what we are looking for
                return cur_path
            # check to see if we have visited the current node.. if not mark it as visited
            if cur_node not in visited:
                visited.add(cur_node)

                # get the neighbors
                neighbors = self.get_neighbors(cur_node)
                # iterate over neighbors
                for n in neighbors:
                    # add the neighbor to the path
                    n_path = cur_path.copy()
                    n_path.append(n)
                    # enqueue the neighbors path
                    q.enqueue(n_path)
       
        return list(visited)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()
        # create a set to hold visited nodes
        visited = set()
        # create a path list to hold the path
        path = [starting_vertex]
        s.push(path)
        # while the queue has something to do....
        while s.size() > 0:
            # grab the path from the stack
            cur_path = s.pop()
            # grab the current node
            cur_node = cur_path[-1]
            # check to see the current node is our destination vertex
            if cur_node == destination_vertex:
                # if it is return it
                return cur_path
            # check to see if the current node has been visited.. 
            if cur_node not in visited: 
                # if not mark it as it has
                visited.add(cur_node)
                # check to see if the current node has any neighbors
                neighbors = self.get_neighbors(cur_node)
                # iterate over the neighbors
                for n in neighbors:
                    n_path = cur_path.copy()
                    # add the neighbor to the paths
                    n_path.append(n)
                    # add the path back to the stack
                    s.push(n_path)
        pass  # TODO
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        visited = [starting_vertex]
        path = []
        new_path = path + visited
        if starting_vertex == destination_vertex:
            return [destination_vertex]
        for neighbor in self.get_neighbors(starting_vertex):
            new_path = self.dfs_recursive(neighbor, destination_vertex)
        if new_path:    
            return new_path
    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None, s=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """

    #     if visited == None:
    #         visited = set()
    #     if path == None:
    #         path = [starting_vertex]
    #     if s == None:
    #         s = Stack()

    #     s.push(path)
    #     # base case: have we reached our destination
    #     if starting_vertex == destination_vertex:
    #         # if so return the constructed path
    #         print(f"reached the end...\t\t {path}")
    #         # cur_path = s.pop()
    #         return path
    #     # check to see if we have been visited
    #     if starting_vertex not in visited:
    #         cur_path = s.pop()
    #         print(cur_path)
    #         cur_node = cur_path[-1]
    #         visited.add(cur_node)
    #         neighbors = self.get_neighbors(cur_node)

    #         for n in neighbors:
    #             n_path = cur_path.copy()
    #             n_path.append(n)

    #             self.dfs_recursive(n, destination_vertex, visited, n_path, s)

    #     # return path
    #     # if we do have neighbors... iterate over them and recurse for each one

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
    print(graph.get_neighbors(2))
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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
