class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        def dfs(coord, i, visted_set):
            nonlocal res
            coords = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if i >= len(word) - 1:
                res = True
                return
            u, v = coord
            for y, x in coords:
                if u + y < 0 or v + x < 0 or u + y >= len(board) or v + x >= len(board[0]):
                    continue
                if board[u + y][v + x] == word[i + 1] and (u + y, v + x) not in visted_set:
                    visted_set.add((u + y, v + x))
                    dfs((u + y, v + x), i + 1, visted_set)
                    visted_set.remove((u + y, v + x))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if res == False and board[i][j] == word[0]:
                    s = set([(i, )])
                    dfs((i, j), 0, s)

        return res