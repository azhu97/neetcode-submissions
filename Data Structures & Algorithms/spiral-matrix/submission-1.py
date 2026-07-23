class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        coords = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        s = set()
        curr = (0, 0)
        direction = 0
        while len(res) < len(matrix) * len(matrix[0]):
            y, x = curr
            # print(y, x)
            if (y, x) not in s:
                res.append(matrix[y][x])
            s.add((y, x))
            # print(u, v)
            u, v = coords[direction]
            u += y
            v += x
            print(u, v)
            if u < 0 or v < 0 or u >= len(matrix) or v >= len(matrix[0]) or (u, v) in s:
                print("First")
                # if you can't proceed, don't add, change direction
                direction += 1
                print(direction)
                direction %= len(coords)
            else:
                print("Second")
                # you can proceed
                curr = (u, v)
        
        # print(res)
        return res