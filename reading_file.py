def read_adjacency_matrix_from_csv(filename: str, directed: bool = False) -> list[list[int]] | None:
    """
    Reads a graph from a CSV file and returns its adjacency matrix.
    The file must contain two columns: source vertex and destination vertex.
    For undirected graphs, edges are mirrored.

    :param filename: Path to the CSV file.
    :param directed: Whether the graph is directed.
    :return: Adjacency matrix as a list of lists, or None if the file is invalid.
    """

    if not isinstance(filename, str) or not filename.strip():
        print("Error: filename must be a non-empty string.")
        return None

    if not filename.lower().endswith(".csv"):
        print(f"Error: file '{filename}' is not a CSV file.")
        return None

    edges = []
    vertices = set()

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                clean = line.strip()

                if not clean or clean.startswith('#'):
                    continue

                parts = clean.split(',')
                if len(parts) != 2:
                    print(f"Line {line_num}: invalid format '{clean}'. Expected 2 columns.")
                    return None

                u = parts[0].strip()
                v = parts[1].strip()

                if not u or not v:
                    print(f"Line {line_num}: empty vertex name in '{clean}'.")
                    return None

                edges.append((u, v))
                vertices.add(u)
                vertices.add(v)

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    if not edges:
        print("Error: the file does not contain any valid edges.")
        return None

    sorted_vertices = sorted(vertices)
    n = len(sorted_vertices)

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    index = {v: i for i, v in enumerate(sorted_vertices)}

    for u, v in edges:
        ui = index[u]
        vi = index[v]
        matrix[ui][vi] = 1
        if not directed:
            matrix[vi][ui] = 1

    return matrix
