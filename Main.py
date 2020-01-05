import networkx as nx

from Node import Node


def read_nodes_from_file(file_nodes):
    node_list = []
    file = open(file_nodes, "r")
    data = file.read().splitlines()
    for node in data:
        long, lat = node.split(' ')
        node_list.append(Node(long, lat))

    file.close()
    return node_list


if __name__ == "__main__":
    print("Hi")
    nodes = read_nodes_from_file('nodes.txt')
    graph = nx.Graph()
    print()
