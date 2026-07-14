class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hashmap = defaultdict(set)

        for row_index, row in enumerate(board):
            row_set = set()

            for coloumn_index, x in enumerate(row):
                if x != ".":
                    coords = tuple((row_index // 3, coloumn_index // 3))

                    if x in row_set or x in hashmap[coords]:
                        return False

                    row_set.add(x)
                    hashmap[coords].add(x)

        for y in range(9):
            coloumn_set = set()

            for x in range(9):
                item = board[x][y]

                if item != ".":
                    if item in coloumn_set:
                        return False

                    coloumn_set.add(board[x][y])
                
        return True
            