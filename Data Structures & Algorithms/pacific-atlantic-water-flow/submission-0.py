class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # heights represents height above sea level at cell (r, c)
        # The island borders the Pacifc from top and the left 
        # The island borders the Atlantic from the bottom and right
        # Water flows up, down, left, right 
        # Find all cells wherew ater can flow from that cell to botht he pacific and atlatnic ocean
        # return as an arr[arrs] that [r, c] can flow from that cell to botht he pacific and atlantic ocean
        # [r, c] = has a path to (top or left border) && (right or left)
        # first solution, run bfs on all pacfic border to see which cells are reachable
        # then run the same thing on the atlantic borders 
        # the solution is the intersection between the two
        # runtime is O((E + V) + (length + height))
        pacific_border, atlantic_border = deque(), deque()
        for i in range(len(heights[0])):
            pacific_border.append((0, i))
            atlantic_border.append((len(heights) - 1, i)) 
        for j in range(len(heights)):
            pacific_border.append((j, 0))
            atlantic_border.append((j, len(heights[0]) - 1))
        
        print(pacific_border)
        print(atlantic_border)
        
        def bfs(que):
            # return the visited set
            coords = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            visted = set()
            while que:
                node = que.popleft()
                visted.add(node)
                i, j = node
                for coord in coords:
                    temp_i, temp_j = i + coord[0], j + coord[1]
                    if temp_i < 0 or temp_i >= len(heights) or temp_j < 0 or temp_j >= len(heights[0]) or (temp_i, temp_j) in visted:
                        continue
                    if heights[i][j] > heights[temp_i][temp_j]:
                        continue
                    if (temp_i, temp_j) == (2, 2):
                        print(i, j)
                    que.append((temp_i, temp_j))
            
            return visted
        p_set, a_set = bfs(pacific_border), bfs(atlantic_border)

        res = []
        for u, v in p_set:
            if (u, v) in a_set:
                res.append([u, v])
        print(p_set)
        print(a_set)
        return res