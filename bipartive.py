from collections import deque

def is_bipartite_matrix(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    colors = [0] * n

    def bfs(start):
        queue = deque([start])
        colors[start] = 1

        while queue:
            node = queue.popleft()

            for neigh in range(n):
                if matrix[node][neigh] != 0:          # є ребро
                    if colors[neigh] == colors[node]:
                        return False
                    if colors[neigh] == 0:
                        colors[neigh] = -colors[node]
                        queue.append(neigh)
        return True

    for v in range(n):
        if colors[v] == 0:
            if not bfs(v):
                return False

    return True
