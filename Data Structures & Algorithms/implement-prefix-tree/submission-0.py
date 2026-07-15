class PrefixTree:

    def __init__(self):
        self.set = set()

    def insert(self, word: str) -> None:
        self.set.add(word)

    def search(self, word: str) -> bool:
        return word in self.set

    def startsWith(self, prefix: str) -> bool:
        for word in self.set:
            if len(word) < len(prefix):
                continue
            if word[:len(prefix)] == prefix:
                return True 
        return False
        
        