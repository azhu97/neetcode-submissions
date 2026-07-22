class WordDictionary:
    class letter:
        def __init__(self):
            self.next_letter = [None] * 26 
            self.end = False

    def __init__(self):
        self.root = self.letter()

    def addWord(self, word: str) -> None:
        # want to craete a chain of letters
        curr = self.root
        for char in word:
            i = ord(char) - ord('a')
            if curr.next_letter[i] is None:
                curr.next_letter[i] = self.letter()
            curr = curr.next_letter[i]
        curr.end = True

    def search(self, word: str) -> bool:
        res = False
        def dfs(i, node):
            nonlocal res
            if i >= len(word) and node.end:
                res = True
                return
            if word[i] == '.':
                for next_letter in node.next_letter:
                    if next_letter:
                        dfs(i + 1, next_letter)
            else:
                next_letter = node.next_letter[ord(word[i]) - ord('a')]
                if next_letter is None:
                    return
                dfs(i + 1, next_letter)
        dfs(0, self.root)
        return res
                