from settings import *
from collections import deque
cols, rows = 31, 28
grid = []
queue, visited = deque(), []
path = []
solution = []

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if MATRIX[i][j] == 0:
            self.wall = True

    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])

for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

start = grid[1][1]
end = grid[1][16]
start.wall = False
end.wall = False

queue.append(start)
start.visited = True


def ucs(end_x, end_y):
    global end
    end = grid[end_x][ end_y]
    flag = False
    noflag = True
    startflag = True

    while True:

        if len(queue) > 0:
            current = queue.popleft()
            if current == end:
                temp = current
                while temp.prev:
                    path.append(temp.prev)
                    temp = temp.prev
                if not flag:
                    flag = True
                    print("Done")
                elif flag:
                    continue
            if flag == False:
                for i in current.neighbors:
                    if not i.visited and not i.wall:
                        i.visited = True
                        i.prev = current
                        queue.append(i)
        else:
            if noflag and not flag:
                print("No Solution", "There was no solution")
                noflag = False
            else:
                continue

        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                if spot in path:
                    solution.append((spot.x,spot.y))
        print(solution)

        if(len(solution)>1):
            break



#ucs()
