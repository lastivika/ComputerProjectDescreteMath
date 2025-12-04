# --------------------------
# I. ДОПОМІЖНІ ФУНКЦІЇ DFS (ДЛЯ ПЕРЕВІРКИ ЗВ'ЯЗНОСТІ/МОСТІВ)
# --------------------------

def dfs_recursive(graph, u, visited):
    """Обхід у глибину для перевірки зв'язності (потрібно для is_bridge)."""
    # Додаємо поточну вершину до відвіданих
    visited.add(u)
    
    # Рекурсивно перевіряємо всіх сусідів
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
    
    # 1. Створюємо копію графа
    temp_graph = {k: list(v) for k, v in g.items()}
    
    # 2. Тимчасово видаляємо ребро (u, v)
    remove_edge(temp_graph, u, v)
    
    # 3. Перевіряємо, чи можемо ми все ще дістатися з u до v
    visited_u = set()
    dfs_recursive(temp_graph, u, visited_u)
    
    # Якщо v не була відвідана після видалення, це міст
    return v not in visited_u

# --------------------------
# II. КРИТЕРІЙ ЕЙЛЕРОВОСТІ
# --------------------------

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

# --------------------------
# III. АЛГОРИТМ ФЛЕРІ (ПОБУДОВА)
# --------------------------

def fleury_algorithm(graph, start_node):
    """
    Алгоритм Флері: будує Ейлерів шлях/цикл, уникаючи мостів.
    """
    current_graph = {k: list(v) for k, v in graph.items()}
    path = []
    u = start_node

    # Цикл працює, поки в графі є невикористані ребра
    while sum(len(v) for v in current_graph.values()) > 0:
        
        neighbors = current_graph.get(u, [])
        if not neighbors: break
        
        selected_edge = None
        
        # Перевіряємо сусідів, застосовуючи правило Флері
        for v in neighbors:
            
            # 1. Якщо це єдине ребро, мусимо його взяти (навіть якщо це міст)
            if len(neighbors) == 1:
                selected_edge = (u, v)
                break
            
            # 2. Якщо є альтернативи, обираємо ребро, яке НЕ Є мостом
            if not is_bridge(current_graph, u, v):
                selected_edge = (u, v)
                break
        
        # Якщо selected_edge досі None, це означає, що всі сусіди є мостами, 
        # і їх більше одного. Просто беремо перший, як останній вибір.
        if not selected_edge:
            v = neighbors[0] 
            selected_edge = (u, v)

        u, v = selected_edge
        path.append(f"{u} -> {v}")
        remove_edge(current_graph, u, v)
        u = v # Переходимо до нової вершини
            
    all_edges_used = sum(len(v) for v in current_graph.values()) == 0
    return path, all_edges_used

# --------------------------
# IV. ТЕСТУВАННЯ
# --------------------------

# Тестовий Граф G2 (Ейлерів шлях, непарні: A, B)
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
    start_node = nodes[0] # Починаємо з непарної вершини
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