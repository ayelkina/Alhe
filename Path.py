class Path:
    cost = 0
    heuristic = 0
    goal = ''
    path = []

    def __init__(self, cost, heuristic, path):
        self.cost = cost
        self.heuristic = heuristic
        self.path = path
        self.goal = cost + heuristic
