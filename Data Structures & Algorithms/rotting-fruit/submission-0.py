from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # grid -> 2D each grid has three possible values
        # 0 -> empty 
        # 1 -> fresh fruit 
        # 2 -> rotten fruit
        # rotten fruit makes fresh fruit rotten 
        # this occurs every seconds tick 
        # get an array of every rotten intial rotten fruit location
        # then a normal bfs function with the rotten fruit array
        # how can we replicate the minute snap shot model? 
        # think about printing level by level
        # think of each second in this model:

        # que 
        # get rid of len(que) amount in que
        # increment second 
        # repeat

        # when # of rotten fruit == # total fruit, we can stop the simulation
        
        fruit_count, rot_count = 0, 0
        que = deque()# holds the coords of rotten fruits
        seconds = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    fruit_count += 1
                if grid[i][j] == 2:
                    rot_count += 1
                    que.append((i, j))
        
        print(que, rot_count, fruit_count)
        COORDS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        # while rotten

        return res