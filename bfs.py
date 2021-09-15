
from collections import deque
from settings import *

wall, clear = 0, 1
width, height = 28, 31

def bfs(grid, start, finish):
    queue = deque([[start]])
    x_finish, y_finish = finish
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == x_finish and y == y_finish:
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

#path = bfs(MATRIX, (1, 1),(1,6))
#print(path)

