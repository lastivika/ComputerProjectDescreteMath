def is_safe(v, adj_list, path, pos):
    u = path[pos - 1]

    if v not in adj_list.get(u, []):
        return False

    if v in path[:pos]:
        return False

    return True

def hamiltonian_util(adj_list, N, path, pos):
    if pos == N:
        if path[0] in adj_list.get(path[N - 1], []):
            return True
        else:
            return False

    for i in range(N):
        if is_safe(i, adj_list, path, pos):
            path[pos] = i

            if hamiltonian_util(adj_list, N, path, pos + 1):
                return True

            path[pos] = -1

    return False

def find_hamiltonian_cycle(adj_list, N):
    path = [-1] * N
    path[0] = 0

    if not hamiltonian_util(adj_list, N, path, 1):
        return "Гамільтонів цикл відсутній."
    else:
        return path + [path[0]]
