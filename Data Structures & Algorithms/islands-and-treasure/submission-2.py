class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # have a bfs function that sets how far something from the parent -> extend from parent
        # collection a list of of treasure locations
        def bfs(coords):
            visited_set = set()
            que = deque(coords)
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            while que:
                temp = que.popleft()
                i, j, step = temp
                grid[i][j] = min(grid[i][j], step)
                visited_set.add((i, j))
                for y, x in directions:
                    ii, jj = i + y, j + x
                    if (ii, jj) in visited_set or ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[0]) or grid[ii][jj] == -1:
                        continue
                    que.append((ii, jj, step + 1))
                    visited_set.add((ii, jj))
                    

        
        LIST = [] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    LIST.append((i, j, 0)) 

        bfs(LIST)