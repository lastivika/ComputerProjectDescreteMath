def dfs_recursive(graph, u, visited):
    """Depth-First Search (DFS) for connectivity check (required for is_bridge)."""
    visited.add(u)
    
    for v in graph.get(u, []):
        if v not in visited:
            dfs_recursive(graph, v, visited)

def get_unique_nodes(graph):
    """Gets all unique vertices (nodes) of the graph."""
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)
    return nodes

def remove_edge(g, u, v):
    """Removes the edge (u, v) from the graph in both directions."""
    if v in g.get(u, []):
        g[u].remove(v)
    if u in g.get(v, []):
        g[v].remove(u)

def is_bridge(g, u, v):
    """KEY CHECK: Determines if the edge (u, v) is a bridge."""
    
    temp_graph = {k: list(v) for k, v in g.items()}
    
    remove_edge(temp_graph, u, v)
    
    visited_u = set()
    dfs_recursive(temp_graph, u, visited_u)
    
    return v not in visited_u

def is_connected(graph):
    """Checks if the graph is connected (for initial verification)."""
    nodes = get_unique_nodes(graph)
    if not nodes: return True
    
    start_node = next(iter(nodes))
    visited = set()
    dfs_recursive(graph, start_node, visited)
    
    active_nodes = {n for n in nodes if n in graph and len(graph[n]) > 0}
    return len(visited) >= len(active_nodes)

def check_euler_criteria(graph):
    """
    UPDATED: Checks the graph only for the existence of an Eulerian CYCLE.
    """
    if not is_connected(graph):
        return 'none', None
        
    odd_degree_vertices = []
    
    for node, neighbors in graph.items():
        degree = len(neighbors)
        if degree % 2 != 0:
            odd_degree_vertices.append(node)
            
    num_odd = len(odd_degree_vertices)
    
    if num_odd == 0:
        return 'cycle', None  
    else:
        return 'none', None  

def fleury_algorithm(graph, start_node):
    """
    Fleury's Algorithm: Constructs an Eulerian path/cycle, avoiding bridges.
    """
    current_graph = {k: list(v) for k, v in graph.items()}
    path = []
    u = start_node

    while sum(len(v) for v in current_graph.values()) > 0:
        
        neighbors = current_graph.get(u, [])
        if not neighbors: break
        
        selected_edge = None
        
        for v in neighbors:
            
            if len(neighbors) == 1:
                selected_edge = (u, v)
                break
        
            if not is_bridge(current_graph, u, v):
                selected_edge = (u, v)
                break
        
        if not selected_edge:
            v = neighbors[0]  
            selected_edge = (u, v)

        u, v = selected_edge
        path.append(u)
        path.append(v)
        remove_edge(current_graph, u, v)
        u = v
            
    all_edges_used = sum(len(v) for v in current_graph.values()) == 0
    final_path = [path[0]] + [path[i] for i in range(1, len(path), 2)]
    return " -> ".join(final_path), all_edges_used

GRAPH_G2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C'],
    'E': ['B', 'C']
}

print("--- ANALYSIS OF GRAPH G2 (FINDING EULERIAN CYCLE) ---")
criteria, _ = check_euler_criteria(GRAPH_G2)

if criteria == 'cycle':
    start_node = next(iter(GRAPH_G2.keys())) 
    euler_path, success = fleury_algorithm(GRAPH_G2, start_node)
    
    if success:
        print(f"Eulerian cycle found. Starting from {start_node}:")
        print(euler_path)
    else:
        print("Failed to construct the cycle, although the parity criteria are met.")
elif criteria == 'path':
    pass  
else:
    print("Neither an Eulerian cycle nor a path (with odd vertices) meets the CYCLE criteria.")

GRAPH_CYCLE = {
    '1': ['2', '3', '4', '5'],
    '2': ['1', '3', '4', '5'],
    '3': ['1', '2', '4', '5'],
    '4': ['1', '2', '3', '5'],
    '5': ['1', '2', '3', '4']
}

print("\n--- ANALYSIS OF GRAPH K5 (Complete graph, all vertices have degree 4) ---")
criteria_k5, _ = check_euler_criteria(GRAPH_CYCLE)

if criteria_k5 == 'cycle':
    start_node_k5 = '1'  
    euler_path_k5, success_k5 = fleury_algorithm(GRAPH_CYCLE, start_node_k5)
    
    if success_k5:
        print(f"Eulerian cycle found. Starting from {start_node_k5}:")
        print(euler_path_k5)
    else:
        print("Failed to construct the cycle.")
else:
    print("Neither a cycle nor a path exists.")
