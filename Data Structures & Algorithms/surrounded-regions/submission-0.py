class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(coords):
            # given coords, return a list of connect "O"
            nonlocal board
            i, j = coords
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            que = deque([(i, j)])
            visited = set()
            while que:
                i, j = que.popleft()
                visited.add((i, j))
                for ii, jj in directions:
                    y, x = i + ii, j + jj
                    # conditions to skip
                    if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]) or (y, x) in visited or board[y][x] != "O":
                        continue
                    que.append((y, x))
            return visited
        
        bad = set()
        for i in range(len(board)):
            j = 0
            if board[i][j] == "O" and (i, j) not in bad:
                temp = bfs((i, j))
                for tup in temp: bad.add(tup)
            j = len(board[0]) - 1
            if board[i][j] == "O" and (i, j) not in bad:
                temp = bfs((i, j))
                for tup in temp: bad.add(tup)
        for j in range(len(board[0])):
            i = 0
            if board[i][j] == "O" and (i, j) not in bad:
                temp = bfs((i, j))
                for tup in temp: bad.add(tup)
            i = len(board) - 1
            if board[i][j] == "O" and (i, j) not in bad:
                temp = bfs((i, j))
                for tup in temp: bad.add(tup)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) in bad or board[i][j] != "O":
                    continue
                temp = bfs((i, j))
                for ii, jj in temp:
                    board[ii][jj] = "X"
                
        