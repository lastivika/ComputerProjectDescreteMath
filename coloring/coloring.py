from visualisator import visualize_graph

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

# idk if we need this 
if __name__ == "__main__":
    my_graph = [
        [1, 2, 5],
        [0, 2, 3],
        [0, 1, 4],
        [1, 4, 5],
        [2, 3, 5],
        [0, 3, 4]
    ]
    solution_colors = [-1] * len(my_graph)

    if solve_coloring(0, my_graph, solution_colors, 3):
        print("Solution found!")
        print(f"Color assignments: {solution_colors}")
        visualize_graph(my_graph, solution_colors)
    else:
        print("No solution exists for 3 colors.")
        visualize_graph(my_graph, None)
