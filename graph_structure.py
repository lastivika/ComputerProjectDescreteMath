def read_graph_csv_to_binary_adjacency_matrix(filename, directed=False):
    """
    Reads a CSV file representing a graph and returns a binary adjacency matrix
    suitable for algorithms like Hamiltonian cycle search.

    Each row in the CSV should contain at least two columns:
        source_vertex, target_vertex
    Optional additional columns (like weights) are ignored.

    :param filename: str, path to the CSV file
    :param directed: bool, True if the graph is directed, False if undirected
    :return: tuple (adj_matrix, vertices)
        adj_matrix: list of lists of int, 0/1 adjacency matrix
        vertices: list of str, sorted list of vertex names
    """
    vertices_set = set()
    edges = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            row = line.strip().split(',')
            if len(row) < 2:
                continue
            from_v = row[0].strip()
            to_v = row[1].strip()
            vertices_set.update([from_v, to_v])
            edges.append((from_v, to_v))

    vertices = sorted(vertices_set)
    index_map = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    adj_matrix = [[0]*n for _ in range(n)]

    for from_v, to_v in edges:
        i = index_map[from_v]
        j = index_map[to_v]
        adj_matrix[i][j] = 1
        if not directed:
            adj_matrix[j][i] = 1

    return adj_matrix, vertices

if __name__ == "__main__":
    adj_matrix, vertices = read_graph_csv_to_binary_adjacency_matrix(
        "graph_data.csv", directed=True
    )
    print("Vertices:", vertices)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)
