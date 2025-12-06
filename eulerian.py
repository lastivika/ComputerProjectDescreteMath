
def dfs_recursive(graph, u, visited):
    """Обхід у глибину для перевірки зв'язності (потрібно для is_bridge)."""
    visited.add(u)
    
    for v in graph.get(u, []):
        if v not in visited:
            dfs_recursive(graph, v, visited)

def get_unique_nodes(graph):
    """Отримує всі унікальні вершини графа."""
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)
    return nodes

def remove_edge(g, u, v):
    """Видаляє ребро (u, v) з графа в обох напрямках."""
    if v in g.get(u, []):
        g[u].remove(v)
    if u in g.get(v, []):
        g[v].remove(u)

def is_bridge(g, u, v):
    """КЛЮЧОВА ПЕРЕВІРКА: Визначає, чи є ребро (u, v) мостом."""
    
    temp_graph = {k: list(v) for k, v in g.items()}
    
    remove_edge(temp_graph, u, v)
    
    visited_u = set()
    dfs_recursive(temp_graph, u, visited_u)
    
    return v not in visited_u

def is_connected(graph):
    """Перевіряє, чи є граф зв'язним (для початкової перевірки)."""
    nodes = get_unique_nodes(graph)
    if not nodes: return True
    
    start_node = next(iter(nodes))
    visited = set()
    dfs_recursive(graph, start_node, visited)
    
    active_nodes = {n for n in nodes if n in graph and len(graph[n]) > 0}
    return len(visited) >= len(active_nodes)


def check_euler_criteria(graph):
    """
    Перевіряє граф на зв'язність і критерії парності.
    """
    if not is_connected(graph):
        return 'none', None
        
    odd_degree_vertices = []
    
    for _, neighbors in graph.items():
        degree = len(neighbors)
        if degree % 2 != 0:
            odd_degree_vertices.append(_)
            
    num_odd = len(odd_degree_vertices)
    
    if num_odd == 0:
        return 'cycle', None
    elif num_odd == 2:
        return 'path', odd_degree_vertices
    else:
        return 'none', None

def fleury_algorithm(graph, start_node):
    """
    Алгоритм Флері: будує Ейлерів шлях/цикл, уникаючи мостів.
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
        path.append(f"{u} -> {v}")
        remove_edge(current_graph, u, v)
        u = v 
            
    all_edges_used = sum(len(v) for v in current_graph.values()) == 0
    return path, all_edges_used

GRAPH_G2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C'],
    'E': ['B', 'C']
}

print("--- АНАЛІЗ ГРАФА G2 (ЕЙЛЕРІВ ШЛЯХ) ---")
criteria, nodes = check_euler_criteria(GRAPH_G2)

if criteria == 'path':
    start_node = nodes[0] 
    euler_path, success = fleury_algorithm(GRAPH_G2, start_node)
    
    if success:
        print(f"✅ Успіх! Ейлерів шлях знайдено. Початок з {start_node}:")
        print(" -> ".join(euler_path))
    else:
        print("❌ Помилка: Не вдалося знайти шлях.")
elif criteria == 'cycle':
    print("Знайдено цикл, можна починати з будь-якої вершини.")
else:
    print("❌ Ні циклу, ні шляху не існує.")
