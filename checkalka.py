'''def isomorfism_check(graph1: dict, graph2: dict) -> bool:
    if all([check_vertices(graph1, graph2),
            check_edges(graph1, graph2),
            check_degrees(graph1, graph2),
            check_connection(graph1) == check_connection(graph2),
            find_diameter_of_graph(graph1) == find_diameter_of_graph(graph2)]) is False:
        print('FUCK')
        return False


    if weisfeiler_lehman_test(graph1, graph2) is False:
        return False

    return True

    if check_vertices(graph1, graph2) is False:
        return 'SHO NAHUi'

    if check_edges(graph1, graph2) is False:
        return 'NE VIRU'

    if check_degrees(graph1, graph2) is False:
        return 'NE MOZHE Bit'

    if check_connection(graph1) == check_connection(graph2) is False:
        return 'NE KONEKT'

    if find_diameter_of_graph(graph1) == find_diameter_of_graph(graph2) is False:
        return 'DIAMETER'

    if weisfeiler_leman_test(graph1, graph2) is False:
        return 'NU NEEEEE'

    return True




def isomorfism_with_claude(graph_1, graph_2):
    k = find_diameter_of_graph(graph_1)
    if k is None:
        k = 4
    if len(graph_1) != len(graph_2):
        return False

    # Ініціалізація: мітки = степені вершин
    labels1 = {v: len(neighbors) for v, neighbors in graph_1.items()}
    labels2 = {v: len(neighbors) for v, neighbors in graph_2.items()}

    for iteration in range(k):
        # Порівняння мультимножин
        multiset1 = sorted(labels1.values())
        multiset2 = sorted(labels2.values())

        if multiset1 != multiset2:
            return False  # Точно НЕ ізоморфні

        # Оновлення міток
        new_labels1 = {}
        for vertex in graph_1:
            old_label = labels1[vertex]
            neighbor_labels = sorted([labels1[n] for n in graph_1[vertex]])
            new_labels1[vertex] = hash((old_label, tuple(neighbor_labels)))

        new_labels2 = {}
        for vertex in graph_2:
            old_label = labels2[vertex]
            neighbor_labels = sorted([labels2[n] for n in graph_2[vertex]])
            new_labels2[vertex] = hash((old_label, tuple(neighbor_labels)))

        # Перевірка стабілізації
        if (sorted(new_labels1.values()) == sorted(labels1.values()) and
            sorted(new_labels2.values()) == sorted(labels2.values())):
            print(f"✓ Стабілізація досягнута на ітерації {iteration}")
            return True

        labels1 = new_labels1
        labels2 = new_labels2

    # Якщо не виявили різниці за iterations ітерацій
    return True


def create_grid(rows, cols):
    """Створює граф решітки."""
    graph = {}
    for i in range(rows):
        for j in range(cols):
            node = i * cols + j + 1
            neighbors = []
            # Верх
            if i > 0:
                neighbors.append((i-1) * cols + j + 1)
            # Низ
            if i < rows - 1:
                neighbors.append((i+1) * cols + j + 1)
            # Ліво
            if j > 0:
                neighbors.append(i * cols + j)
            # Право
            if j < cols - 1:
                neighbors.append(i * cols + j + 2)
            graph[node] = neighbors
    return graph



print(weisfeiler_leman_test(iso_petersen_1, iso_petersen_2), 'MOEeeeeeeeee')
print(isomorfism_with_claude(iso_petersen_1, iso_petersen_2), 'KLODIK))))))')

import networkx as nx
from collections import Counter

G1 = nx.Graph(iso_petersen_1)
G2 = nx.Graph(iso_petersen_2)

print("РЕЗУЛЬТАТ:")
print(f"NetworkX: {nx.is_isomorphic(G1, G2)}")

# Якщо True, показуємо відображення
if nx.is_isomorphic(G1, G2):
    matcher = nx.isomorphism.GraphMatcher(G1, G2)
    print("\nВідображення:")
    for k, v in sorted(matcher.mapping.items()):
        print(f"  {k} → {v}", 'NE MOE')
'''
