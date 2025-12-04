
def is_safe(v, adj_matrix, path, pos):
    if adj_matrix[path[pos - 1]][v] == 0:
        return False
    if v in path[:pos]:
        return False
    return True

def hamiltonian_util(adj_matrix, N, path, pos):
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
    path = [-1] * N
    path[0] = 0

    if not hamiltonian_util(adj_matrix, N, path, 1):
        return "Гамільтонів цикл відсутній."
    else:
        return path + [path[0]]
