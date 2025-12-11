def is_safe(v, adj_matrix, path, pos):
    """
    Check if a vertex can be added to the current Hamiltonian path.

    :param v: int, the vertex to check
    :param adj_matrix: list[list[int]], adjacency matrix of the graph
    :param path: list[int], current Hamiltonian path
    :param pos: int, current position in the path
    :return: bool, True if the vertex can be added, False otherwise
    """
    if adj_matrix[path[pos - 1]][v] == 0:
        return False
    if v in path[:pos]:
        return False
    return True


def hamiltonian_util(adj_matrix, N, path, pos):
    """
    Recursive utility function to find Hamiltonian cycle.

    :param adj_matrix: list[list[int]], adjacency matrix of the graph
    :param N: int, number of vertices
    :param path: list[int], current Hamiltonian path
    :param pos: int, current position in the path
    :return: bool, True if Hamiltonian cycle exists from current path, False otherwise
    """
    if pos == N:
        if adj_matrix[path[N - 1]][path[0]] == 1:
            return True
        else:
            return False

    for i in range(N):
        if is_safe(i, adj_matrix, path, pos):
            path[pos] = i
            if hamiltonian_util(adj_matrix, N, path, pos + 1):
                return True
            path[pos] = -1

    return False


def find_hamiltonian_cycle(adj_matrix, N):
    """
    Find a Hamiltonian cycle in a graph represented by an adjacency matrix.

    :param adj_matrix: list[list[int]], adjacency matrix of the graph
    :param N: int, number of vertices
    :return: list[int] representing the Hamiltonian cycle including return to start,
             or str message if no Hamiltonian cycle exists
    """
    path = [-1] * N
    path[0] = 0

    if not hamiltonian_util(adj_matrix, N, path, 1):
        return "Hamiltonian cycle does not exist."
    else:
        return path + [path[0]]
