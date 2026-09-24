class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        for i in grid:
            print(i)
        # dijkstras with time as edges
        # take the max instead of summation
        # let the heap be (time, (coords))
        coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set() # holds coords
        heap = []
        heapq.heappush(heap, (grid[0][0], (0, 0)))
        while heap and len(visited) <= (len(grid) * len(grid[0])):
            time, coord = heapq.heappop(heap)
            if coord == (len(grid) - 1, len(grid[0]) - 1):
                return time
            if coord in visited:
                continue
            else:
                visited.add((coord))
            for y, x in coords:
                i, j = coord[0] + y, coord[1] + x
                if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited:
                    continue
                # elevation of both squares is less than or equal to the water level at time t.
                heapq.heappush(heap, (max(time, grid[i][j]), (i, j)))
        
        return -1
            