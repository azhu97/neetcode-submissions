from collections import deque
from typing import List


class Solution:

  def numIslands(self, grid: List[List[str]]) -> int:
    def bfs(r, c):
      que = deque([(r, c)])
      grid[r][c] = "0"  # Mark start cell immediately

      directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      while que:
        i, j = que.popleft()
        for y, x in directions:
          ii, jj = i + y, j + x
          if (
              0 <= ii < len(grid)
              and 0 <= jj < len(grid[0])
              and grid[ii][jj] == "1"
          ):
            grid[ii][jj] = "0"  # Mark visited IMMEDIATELY on append
            que.append((ii, jj))

    res = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == "1":
          res += 1
          bfs(i, j)

    return res