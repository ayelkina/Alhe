import copy

from networkx import Graph

from Path import Path


class Astar:
    expanded_nodes = 0
    solution = []

    def solve(self, graph: Graph, edges: list):
        input_nodes = list(graph.nodes)
        nodes_number = len(input_nodes)
        first_node = input_nodes[0]
        open_set = [Path(0, 0, [first_node], edges)]

        while open_set:
            self.solution = self.minimal_solution(open_set)
            last_node = self.solution.path[-1]
            if len(self.solution.path) == nodes_number and last_node == first_node:
                break
            if len(self.solution.path) == nodes_number and last_node != first_node:
                self.solution.path.remove(first_node)
            for neigh in graph.adj[last_node].items():
                node = neigh[0]
                cost = neigh[1]['weight']
                if node in self.solution.path: continue
                sum_cost = self.solution.cost + cost
                new_path = self.solution.path + [node]
                not_used_edges = self.solution.not_used_edges[:]
                not_used_edges.remove(cost)
                heuristic = self.heuristic_fun(not_used_edges, nodes_number, len(new_path)-1)
                open_set.append(Path(sum_cost, heuristic, new_path, not_used_edges))
            self.expanded_nodes += 1

    @staticmethod
    def minimal_solution(open_set: list):
        min_cost = 9999999999
        solution = ''
        for state in open_set:
            if state.goal < min_cost:
                min_cost = state.goal
                solution = state
        open_set.remove(solution)
        return solution

    @staticmethod
    def heuristic_fun(edges: list, n: int, k: int):
        sum = 0
        nodes_left = n-k
        for index in range(nodes_left):
            sum += edges[index]

        return sum
