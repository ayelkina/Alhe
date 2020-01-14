import math

from networkx import Graph

from Path import Path


class Astar:
    expanded_nodes = 0
    solution = []

    def solve(self, graph: Graph, edges: list):
        self._solve(graph, edges)
        print('cost={}, solution={}'.format(self.solution.cost, self.solution.path))
        print("expanded nodes", self.expanded_nodes)

    def _solve(self, graph: Graph, edges: list):
        input_nodes = list(graph.nodes)
        nodes_number = len(input_nodes)
        first_node = input_nodes[0]
        open_set = [Path(0, 0, [first_node])]
        expanded = []

        while open_set:
            self.solution = self.minimal_solution(open_set)
            last_node = self.solution.path[-1]
            if self.solution.path in expanded:
                continue

            if len(self.solution.path) == nodes_number:
                if last_node == first_node:
                    self.solution.path = [first_node] + self.solution.path
                    break
                elif self.solution.path[0] == first_node:
                    self.solution.path.remove(first_node)
                else:
                    continue
            neighbours = graph.adj[last_node].items()
            for neigh in neighbours:
                node = neigh[0]
                if node in self.solution.path:
                    continue
                sum_cost = self.solution.cost + neigh[1]['weight']
                new_path = self.solution.path + [node]
                heuristic = self.heuristic_fun(edges, nodes_number, len(new_path) - 1)
                next_solution = Path(sum_cost, heuristic, new_path)
                open_set.append(next_solution)
            self.expanded_nodes += 1
            expanded.append(self.solution.path)

        if len(open_set) == 0:
            self.solution.cost = math.inf
            self.solution.path = []

    @staticmethod
    def minimal_solution(open_set: list):
        min_cost = math.inf
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
        nodes_left = n - k
        for index in range(nodes_left):
            sum += edges[index]

        return sum
