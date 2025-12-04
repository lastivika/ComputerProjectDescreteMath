import networkx as nx
import matplotlib.pyplot as plt


def is_safe(node, color, graph, colors):
    """
    Check if it is safe to assign 'color' to 'node'.
    It is safe if no neighbor has the same color.
    """
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def solve_coloring(node, graph, colors, num_colors):
    """
    Recursive backtracking function.
    Returns True if coloring is possible, False otherwise.
    """
    # Base Case: If we have colored all nodes (index reached end), we are done
    if node == len(graph):
        return True

    # Try every color from 0 to num_colors-1
    for color in range(num_colors):
        if is_safe(node, color, graph, colors):
            colors[node] = color # assign color

            # recursion to the next node
            if solve_coloring(node + 1, graph, colors, num_colors):
                return True

            # backt4rack: if the choice didn't lead to a solution, undo it
            colors[node] = -1

    return False
