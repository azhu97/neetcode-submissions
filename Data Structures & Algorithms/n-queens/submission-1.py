class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        config = ["." * i + "Q" + "." * (n - i - 1) for i in range(n)]
        # now we want to try every permuation
        # where we use every row exactly once
        # then we run a check to see if its valid, if valid we add a copy
        res = []
        def check(board):
            # return true if valid board
            # false otherwise 
            for i, row in enumerate(board):
                # find the queen
                # guranteed no row conlict
                j = row.find("Q")
                # board[i][j] == "Q"
                # for ii in range(n):
                #     if ii == i:
                #         continue
                #     if board[ii][j] == "Q":
                #         return False
                # check upper right 
                ii, jj = i, j
                for _ in range(n):
                    ii -= 1
                    jj += 1
                    if ii < 0 or jj >= n:
                        break
                    if board[ii][jj] == "Q":
                        # print("upper right")
                        return False
                # check upper left
                ii, jj = i, j
                for _ in range(n):
                    ii -= 1
                    jj -= 1
                    if ii <= 0 or jj <= 0:
                        break
                    if board[ii][jj] == "Q":
                        # print("upper left")
                        return False
                # check bottom left 
                ii, jj = i, j
                for _ in range(n):
                    ii += 1
                    jj -= 1
                    if ii >= n or jj < 0:
                        break
                    if board[ii][jj] == "Q":
                        # print("bottom left, ", ii, jj, i, j)
                        return False
                # check bottom right
                ii, jj = i, j 
                for _ in range(n):
                    ii += 1
                    jj += 1
                    if ii >= n or jj >= n:
                        break
                    if board[ii][jj] == "Q":
                        # print("bottom right")
                        return False
            return True

        def permutate(marking, arr):
            nonlocal config
            nonlocal res
            if len(arr) >= len(marking):
                if check(arr):
                    res.append(arr.copy())
                return
            for i, mark in enumerate(marking):
                if mark:
                    # mark, include, run, restore
                    marking[i] = 0
                    arr.append(config[i])
                    permutate(marking, arr)
                    marking[i] = 1
                    arr.pop()
        
        permutate([1 for i in range(n)], [])
        return res
