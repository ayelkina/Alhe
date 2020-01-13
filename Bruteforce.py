import math

from networkx import Graph


class Bruteforce:

    min_cost = math.inf
    solution = []
    count = 0

    def solve(self, graph: Graph, first_node):
        self.min_cost = math.inf
        self.solution = []
        self._solve(graph, first_node, first_node, [], 0)
        print('cost={}, solution={}'.format(self.min_cost, self.solution))
        print('expanded nodes', self.count)

    def _solve(self, graph: Graph, first_node, cur_node, visited_nodes: list, cost):
        self.count += 1

        if len(visited_nodes) == len(graph.nodes):
            if visited_nodes[-1] == first_node and cost < self.min_cost:
                self.min_cost = cost
                self.solution = [first_node] + visited_nodes
            return

        for node, attrs in graph.adj[cur_node].items():
            if node not in visited_nodes:
                self._solve(graph, first_node, node, visited_nodes + [node], cost + attrs['weight'])
