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
    if isinstance(graph, list):
        graph_dict = {}
        for i in range(len(graph)):
            graph_dict[i] = []

        all_vertices = list(graph_dict.keys())

        for ind, row in enumerate(graph):
            for indx, element in enumerate(row):
                if element == 1:
                    graph_dict[all_vertices[ind]].append(all_vertices[indx])

        graph = graph_dict



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

    '''all_edges_used = sum(len(v) for v in current_graph.values()) == 0'''
    final_path = [path[0]] + [path[i] for i in range(1, len(path), 2)]
    '''return " -> ".join(final_path), all_edges_used'''
    return final_path
