class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        for edge in edges:
            a, b = edge
            if a in visited and b in visited:
                return edge
            visited.add(a)
            visited.add(b)
        return [-1, -1]