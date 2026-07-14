class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        m = 0

        def bfs(r, c):
            print(1)
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            count = 1
            
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    rr, cc = i + di, j + dj
                    if rr >= ROWS or cc >= COLS or rr < 0 or cc < 0 or grid[rr][cc] == 0:
                        continue
                    grid[rr][cc] = 0
                    q.append((rr, cc))
                    count += 1

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    tc = bfs(r, c)
                    m = max(m, tc)
        
        return m 

                

        