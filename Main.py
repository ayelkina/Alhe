import time

from Astar import Astar
from Bruteforce import Bruteforce
from Greedy import Greedy
from NetworkParser import NetworkParser

if __name__ == "__main__":
    parser = NetworkParser()
    graph = parser.load_graph_from_txt("links_big.txt")
    # graph = parser.load_graph_from_xml("janos-us.xml")

    astar = Astar()
    bruteforce = Bruteforce()
    greedy = Greedy()

    start_greedy = time.time()
    greedy.solve(graph, list(graph.nodes)[0])
    end_greedy = time.time()
    print("greedy time", end_greedy - start_greedy, '\n')

    start_astar = time.time()
    astar.solve(graph, parser.sorted_costs)
    end_astar = time.time()
    print("A* time", end_astar - start_astar, '\n')

    start_brute = time.time()
    bruteforce.solve(graph, list(graph.nodes)[0])
    end_brute = time.time()
    print("bruteforce time", end_brute - start_brute, '\n')

















