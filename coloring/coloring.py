from visualisator import visualize_graph

def read_adjacency_matrix(filename: str):
    """
    Reads adjacency matrix from a file and converts it to adjacency list.
    """
    matrix = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            row = list(map(int, line.split()))
            matrix.append(row)

    # convert adjacency matrix to adjacency list
    adj_list = []
    for i in range(len(matrix)):
        neighbors = []
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                neighbors.append(j)
        adj_list.append(neighbors)

    return adj_list

def is_safe(node, color, graph, colors) -> bool:
    """
    Check if it is safe to assign 'color' to 'node'.
    It is safe if no neighbor has the same color.
    """
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve_coloring(node, graph, colors, num_colors) -> bool:
    """
    Recursive backtracking function.
    Returns True if coloring is possible, False otherwise.
    """
    # if we have colored all nodes (index reached end), we are done
    if node == len(graph):
        return True

    # try every color from 0 to num_colors-1
    for color in range(num_colors):
        if is_safe(node, color, graph, colors):
            colors[node] = color # assign color

            # recursion to the next node
            if solve_coloring(node + 1, graph, colors, num_colors):
                return True

            # backtrack: if the choice didn't lead to a solution, undo it
            colors[node] = -1

    return False


if __name__ == "__main__":
    filename = "graph_matrix.txt" #====================

    graph = read_adjacency_matrix(filename)
    colors = [-1] * len(graph)

    if solve_coloring(0, graph, colors, 3):
        print("Solution found!")
        print("Colors:", colors)
        visualize_graph(graph, colors)
    else:
        print("No 3-coloring possible.")
        visualize_graph(graph, None)
