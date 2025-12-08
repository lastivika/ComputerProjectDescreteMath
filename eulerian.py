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
    ОНОВЛЕНО: Перевіряє граф лише на існування Ейлерового ЦИКЛУ.
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

print("--- АНАЛІЗ ГРАФА G2 (ПОШУК ЕЙЛЕРОВОГО ЦИКЛУ) ---")
criteria, _ = check_euler_criteria(GRAPH_G2)

if criteria == 'cycle':
    start_node = next(iter(GRAPH_G2.keys())) 
    euler_path, success = fleury_algorithm(GRAPH_G2, start_node)
    
    if success:
        print(f"Ейлерів цикл знайдено. Початок з {start_node}:")
        print(euler_path)
    else:
        print("Не вдалося побудувати цикл, хоча критерії парності виконані.")
elif criteria == 'path':
    pass 
else:
    print("Ні Ейлерового циклу, ні шляху (з непарними вершинами) не відповідає критеріям ЦИКЛУ.")

GRAPH_CYCLE = {
    '1': ['2', '3', '4', '5'],
    '2': ['1', '3', '4', '5'],
    '3': ['1', '2', '4', '5'],
    '4': ['1', '2', '3', '5'],
    '5': ['1', '2', '3', '4']
}

print("\n--- АНАЛІЗ ГРАФА K5 (Повний граф, всі вершини мають степінь 4) ---")
criteria_k5, _ = check_euler_criteria(GRAPH_CYCLE)

if criteria_k5 == 'cycle':
    start_node_k5 = '1' 
    euler_path_k5, success_k5 = fleury_algorithm(GRAPH_CYCLE, start_node_k5)
    
    if success_k5:
        print(f"Ейлерів цикл знайдено. Початок з {start_node_k5}:")
        print(euler_path_k5)
    else:
        print("Не вдалося побудувати цикл.")
else:
    print("Ні циклу, ні шляху не існує.")
