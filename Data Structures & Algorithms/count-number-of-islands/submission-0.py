class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        count = 0
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    rrow, ccol = row + dr, col + dc
                    if (
                        0 <= rrow < num_rows and
                        0 <= ccol < num_cols and
                        grid[rrow][ccol] == "1"
                    ):
                        grid[rrow][ccol] = "0"
                        q.append((rrow, ccol))

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1

        return count

            
            
            

        
        