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

def read_csv_to_graph(filename, directed=False):
    """
    Reads a CSV file and creates a graph dictionary.
    CSV format: first column = source, second column = destination, optional third column = weight.
    Returns a graph dictionary compatible with other functions.
    """
    import csv

    graph = create_graph(directed=directed)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line_num, row in enumerate(reader, 1):
                if not row or row[0].startswith('#'):
                    continue

                if len(row) < 2:
                    print(f"Line {line_num}: not enough data, skipping.")
                    continue

                from_v = row[0].strip()
                to_v = row[1].strip()

                if not from_v or not to_v:
                    print(f"Line {line_num}: empty vertex name, skipping.")
                    continue

                weight = 1
                if len(row) >= 3:
                    try:
                        weight = float(row[2])
                    except ValueError:
                        print(f"Line {line_num}: invalid weight '{row[2]}', using 1.")
                        weight = 1

                add_edge(graph, from_v, to_v, weight)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    return graph

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
    print("GRAPH INFO:")
    print("=" * 40)
    print(f"Vertices: {len(graph['vertices'])}")
    print(f"Edges: {len(graph['edges'])}")
    print(f"Type: {'Directed' if graph['directed'] else 'Undirected'}\n")

    print("Adjacency List:")
    for vertex in sorted(graph['vertices'].keys()):
        neighbors = graph['vertices'][vertex]
        if neighbors:
            neighbors_str = ", ".join([f"{n}({w})" for n, w in neighbors])
            print(f"  {vertex} -> {neighbors_str}")
        else:
            print(f"  {vertex} -> None")

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
    new_graph['vertices'] = {v: list(neigh) for v, neigh in graph['vertices'].items()}
    new_graph['edges'] = list(graph['edges'])
    return new_graph

def main():
    filename = "graph_data.csv"  # replace with any CSV file
    g = read_csv_to_graph(filename, directed=False)

    if not g:
        print("Failed to create graph.")
        return

    print_graph_info(g)
    print(f"\nVertices: {get_vertices(g)}")
    print(f"Edges: {get_edges(g)}")

    sample_vertex = get_vertices(g)[0]
    print(f"Neighbors of {sample_vertex}: {get_neighbors(g, sample_vertex)}")
    print(f"Degree of {sample_vertex}: {vertex_degree(g, sample_vertex)}")

    matrix, vertices = get_adjacency_matrix(g)
    print(f"\nAdjacency Matrix ({len(matrix)}x{len(matrix)}):")
    for i in range(len(matrix)):
        print(f"  {vertices[i]}: {matrix[i]}")

    g2 = copy_graph(g)
    print(f"\nGraph copy created: {len(g2['vertices'])} vertices")

if __name__ == "__main__":
    main()
