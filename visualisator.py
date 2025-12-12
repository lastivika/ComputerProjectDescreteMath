import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(adj_list, color_assignments=None):
    """
    Draws the graph using NetworkX and Matplotlib.
    """
    # 1. Creates empty graph
    G = nx.Graph()

    # 2. Add edges from our adjacency list
    for node, neighbors in enumerate(adj_list):
        for neighbor in neighbors:
            G.add_edge(node, neighbor) # (NetworkX handles duplicates automatically)

    # 3. Define layout (how nodes are positioned)
    pos = nx.spring_layout(G, 50)

    # 4. Map the integer result (0, 1, 2) to actual colors
    visual_colors = ['lightgray'] * len(adj_list) # default to gray

    if color_assignments:
        color_map = {0: "#FF1D1D", 1: "#2448FF", 2: "#19B83E"} # Red, Blue, Green
        visual_colors = [color_map.get(c, 'black') for c in color_assignments]

    # 5. Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos,
            node_color=visual_colors,
            node_size=800,
            width=2)

    if color_assignments:
        plt.title("Graph Successfully Colored (3 Colors)")
    else:
        plt.title("No Solution Found")

    plt.show()
