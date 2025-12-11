def create_graph(directed=False):
    graph = {
        'vertices': {},
        'edges': [],
        'directed': directed
    }
    return graph

def add_vertex(graph, vertex_name):
    if vertex_name not in graph['vertices']:
        graph['vertices'][vertex_name] = []
        return True
    return False

def add_edge(graph, from_v, to_v, weight=1):
    add_vertex(graph, from_v)
    add_vertex(graph, to_v)
    
    graph['vertices'][from_v].append((to_v, weight))
    
    if not graph['directed']:
        graph['vertices'][to_v].append((from_v, weight))
    
    edge = (from_v, to_v, weight)
    if edge not in graph['edges']:
        graph['edges'].append(edge)
    
    return True

def get_vertices(graph):
    return list(graph['vertices'].keys())

def get_edges(graph):
    return graph['edges']

def get_neighbors(graph, vertex):
    if vertex in graph['vertices']:
        return graph['vertices'][vertex]
    return []

def has_edge(graph, from_v, to_v):
    if from_v not in graph['vertices']:
        return False
    
    for neighbor, _ in graph['vertices'][from_v]:
        if neighbor == to_v:
            return True
    return False

def vertex_degree(graph, vertex):
    if vertex in graph['vertices']:
        return len(graph['vertices'][vertex])
    return 0

def is_connected(graph, start, end):
    visited = set()
    
    def dfs(current):
        if current == end:
            return True
        visited.add(current)
        for neighbor, _ in graph['vertices'][current]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    
    return dfs(start)

def print_graph_info(graph):
    print("=" * 40)
    print("ГРАФ:")
    print("=" * 40)
    print(f"Вершин: {len(graph['vertices'])}")
    print(f"Ребер: {len(graph['edges'])}")
    print(f"Тип: {'Орієнтований' if graph['directed'] else 'Неорієнтований'}")
    
    print("\nСписок суміжності:")
    for vertex in sorted(graph['vertices'].keys()):
        neighbors = graph['vertices'][vertex]
        if neighbors:
            neighbors_str = ", ".join([f"{n}({w})" for n, w in neighbors])
            print(f"  {vertex} -> {neighbors_str}")
        else:
            print(f"  {vertex} -> немає сусідів")

def get_adjacency_matrix(graph):
    vertices = sorted(get_vertices(graph))
    n = len(vertices)
    
    matrix = [[0] * n for _ in range(n)]
    index_map = {vertex: i for i, vertex in enumerate(vertices)}
    
    for from_v in graph['vertices']:
        for to_v, weight in graph['vertices'][from_v]:
            i = index_map[from_v]
            j = index_map[to_v]
            matrix[i][j] = weight
    
    return matrix, vertices

def copy_graph(graph):
    new_graph = create_graph(graph['directed'])
    
    new_graph['vertices'] = {}
    for vertex in graph['vertices']:
        new_graph['vertices'][vertex] = list(graph['vertices'][vertex])
    
    new_graph['edges'] = list(graph['edges'])
    
    return new_graph

def main():
    print("СТРУКТУРА ГРАФА БЕЗ КЛАСІВ")
    print("=" * 50)
    
    g = create_graph(directed=False)
    
    add_edge(g, "A", "B", 5)
    add_edge(g, "A", "C", 3)
    add_edge(g, "B", "D", 2)
    add_edge(g, "C", "D", 1)
    
    print_graph_info(g)
    
    print(f"\nВершини: {get_vertices(g)}")
    print(f"Ребра: {get_edges(g)}")
    print(f"Сусіди A: {get_neighbors(g, 'A')}")
    print(f"Ступінь B: {vertex_degree(g, 'B')}")
    print(f"Чи є ребро A-B: {has_edge(g, 'A', 'B')}")
    print(f"Чи з'єднані A-D: {is_connected(g, 'A', 'D')}")
    
    matrix, vertices = get_adjacency_matrix(g)
    print(f"\nМатриця суміжності ({len(matrix)}x{len(matrix)}):")
    for i in range(len(matrix)):
        print(f"  {vertices[i]}: {matrix[i]}")
    
    g2 = copy_graph(g)
    print(f"\nКопія створена: {len(g2['vertices'])} вершин")

if __name__ == "__main__":
    main()
