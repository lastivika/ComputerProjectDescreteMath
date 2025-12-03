from collections import deque
from utils import Graph # import graph from external file (Daniil does)

def is_bipartite(graph: Graph) -> bool:
    num_vertices = len(graph)
    # 0: unvisited, 1: color A, -1: color B
    colors = [0] * num_vertices

    def bfs(node):
        if colors[node] != 0:
            return True
        queue = deque([node])
        colors[node] = 1

        while queue:
            curr_node = queue.popleft()
            for neighbour in graph[curr_node]:
                # if neigh has the same color - not biparte
                if colors[neighbour] == colors[curr_node]:
                    return False
                # if neigh was not visited.- give opposite color
                elif colors[neighbour] == 0:
                    colors[neighbour] = (-1) * colors[curr_node]
                    queue.append(neighbour)
        return True

    for i in range(num_vertices):
        # start BFS only when node is unvisited
        if colors[i] == 0:
            if not bfs(i):
                return False

    return True
