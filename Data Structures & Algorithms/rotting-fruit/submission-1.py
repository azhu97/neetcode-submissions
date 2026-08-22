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
        COORDS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        print(rot_count, fruit_count, que)
        while rot_count < fruit_count:
            if len(que) == 0:
                return -1
            print("seconds :", seconds)
            seconds += 1
            cycle = len(que)
            for _ in range(cycle):
                i, j = que.popleft()
                print(i, j)
                for y, x in COORDS:
                    t_i, t_j = i + y, j + x # new coord
                    if t_i < 0 or t_i >= len(grid) or t_j < 0 or t_j >= len(grid[0]) or grid[t_i][t_j] != 1:
                        print(f'Skippings {t_i}, {t_j}')
                        continue
                    que.append((t_i, t_j))
                    grid[t_i][t_j] = 2
                    rot_count += 1
        return seconds