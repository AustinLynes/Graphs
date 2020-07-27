from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    # create graph and create path
    anc_graph = Graph()
    paths = []
    
    # add verticies
    for vertex in range(0, 20):
        anc_graph.add_vertex(vertex)
    
    # add edges
    for ancestor in ancestors:
        anc_graph.add_edge(ancestor[0], ancestor[1])
        
    
    # add path to ancestor paths
    for vertex in anc_graph.vertices:
        if anc_graph.dfs(vertex, starting_node) is not None and len(anc_graph.dfs(vertex, starting_node)) > 0:
            paths.append(anc_graph.dfs(vertex, starting_node))
            
    if len(paths) == 1:
        return -1
     
    # find earliest neighbor
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(start_path) and path[0] < start_path[0]:
            start_path = path

    return start_path[0]    
    

