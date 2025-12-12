import argparse

import graph_structure
import isomorfism
import hamilton
import eulerian
import bipartive


parser = argparse.ArgumentParser(description='Change substring')


parser.add_argument('filename_1', help='Name of the first CSV file with graph')
parser.add_argument('function', choices = ["check_isomorfism", "find_hamiltonian", "find_eulerian",\
 "is_bipartite"], help='Function which should be called')
parser.add_argument('--filename_2', help='Name of the second CSV file with graph')


args = parser.parse_args()

filename1 = args.filename_1
filename2 = args.filename_2
function = args.function


graph_1 = graph_structure.get_adjacency_matrix(graph_structure.read_csv_to_graph(filename1))

if function == 'check_isomorfism':
    if filename2 is None:
        raise SystemExit('При check_isomorfism потрібно вказати другий файл з графом (--filename_2)')
    graph_2 = graph_structure.get_adjacency_matrix(graph_structure.read_csv_to_graph(filename2))
    checker = isomorfism.isomorfism_check(graph_1, graph_2)
    if checker:
        print('Графи ізоморфні')
    else:
        print('Графи не ізоморфні')

if function == 'find_hamiltonian':
    print(hamilton.find_hamiltonian_cycle(graph_1))

if function == 'find_eulerian':
    print(eulerian.fleury_algorithm(graph_1, 0))

if function == 'is_bipartite':
    checker = bipartive.is_bipartite_matrix(graph_1)
    if checker:
        print('Граф двочастковий')
    else:
        print('Граф не двочастковий')
