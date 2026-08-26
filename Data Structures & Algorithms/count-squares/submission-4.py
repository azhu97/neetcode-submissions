class CountSquares:

    def __init__(self):
        self.coords = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.coords[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        # print(f"Counting for: {point}")
        # print(f"Current coords: {self.coords}")
        res = 0
        x, y = point[0], point[1]
        keys = list(self.coords.keys())
        for j, i  in keys:
            if self.coords[(j, i)] == 0 or (j == x and i == y):
                continue
            if x != j and y != i and (abs(x - j) != abs(y - i)):
                # square not possible
                continue
            dist = 0
            if x == j:
                dist = abs(y - i)
            else:
                dist = abs(x - j)
            # top left
            res += self.coords[(x-dist, y)]*self.coords[(x-dist, y+dist)]*self.coords[(x, y+dist)]
            # top right
            res += self.coords[(x+dist, y)]*self.coords[(x+dist, y+dist)]*self.coords[(x, y+dist)]
            # bottom left
            res += self.coords[(x-dist, y)]*self.coords[(x-dist, y-dist)]*self.coords[(x, y-dist)]
            # bottom right
            res += self.coords[(x+dist, y)]*self.coords[(x+dist, y-dist)]*self.coords[(x, y-dist)]
        # print(f"res: {res // 3}")
        return res // 3