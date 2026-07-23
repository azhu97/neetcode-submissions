class Solution:
    class Trie:
        def __init__(self):
            self.next_letter = [None] * 26 
            self.end = False
            self.word = None

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def add_word_to_root(word, root):
            curr = root
            for let in word:
                i = ord(let) - ord('a')
                if curr.next_letter[i] is None:
                    curr.next_letter[i] = self.Trie()
                curr = curr.next_letter[i] 
            curr.end, curr.word = True, word
            print(curr.word)
        def dfs(coord, visited_set, node, print_flag):
            nonlocal res 
            if node.end:
                res.add(node.word)
            coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited_set.add(coord)
            u, v = coord
            if print_flag: print(board[u][v])
            for y, x in coords:
                if u + y < 0 or v + x < 0 or u + y >= len(board) or v + x >= len(board[0]) or (u + y, v + x) in visited_set:
                    continue
                # one more check
                i = ord(board[u + y][v + x]) - ord('a')
                if node.next_letter[i]:
                    dfs((u + y, v + x), visited_set, node.next_letter[i], print_flag)
                    # print((u + y, v + x) in visited_set)
            
        res = set()
        root = self.Trie()
        for word in words:
            add_word_to_root(word, root)               
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                order = ord(board[i][j]) - ord('a')
                if root.next_letter[order]:
                    print(f"Starting DFS at {board[i][j]}, {(i, j)}")
                    dfs((i, j), set(), root.next_letter[order], True)

        return list(res)