class Node:
    id = ''
    long = ''
    lat = ''

    def __init__(self, id, long, lat):
        self.id = int(id)
        self.long = float(long)
        self.lat = float(lat)