class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(coords):
            nonlocal board
            que = deque(coords)
            visited = set()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while que:
                i, j = que.popleft()
                visited.add((i, j))

                for ii, jj in directions:
                    y, x = i + ii, j + jj
                    if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]) or (y, x) in visited or board[y][x] != "O":
                        continue
                    # otherwise we add it to the que
                    que.append((y, x))
            
            return visited

        temp_coords = []
        for i in range(len(board)):
            if board[i][0] == "O":
                temp_coords.append((i, 0))
            if board[i][len(board[0]) - 1] == "O":
                temp_coords.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            if board[0][j] == "O":
                temp_coords.append((0, j))
            if board[len(board) - 1][j] == "O":
                temp_coords.append((len(board) - 1, j))
        bad = bfs(temp_coords)
        good = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "O" or (i, j) in bad:
                    continue
                good.append((i, j))
        good = bfs(good)
        for i, j in good:
            board[i][j] = "X"
        
        

