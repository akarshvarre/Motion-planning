#2D grid
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]


init = [2, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

def heuristic_func ():
    
    expand = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    expand[goal[0]][goal[1]] = 1
    
    heuristic_matrix = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    cost = 0
    
    list = []
    list.append([0,goal[0],goal[1]])
    
    while (len(list) != 0):
        for i in range(len(delta)):
            x = list[0][1] + delta[i][0]
            y = list[0][2] + delta[i][1]
    
            if x >= 0 and x < len(grid) and y >=0 and y < len(grid[0]):
                if expand[x][y] == 0:
                    g = list[0][0] + 1
                    list.append([g,x,y])
                    heuristic_matrix[x][y] = g
                    expand[x][y] = 1
        list.pop(0)
                    
    return (heuristic_matrix)

heuristic = heuristic_func()


def search(grid,init,goal):
 
 
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    distance = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    f = heuristic[x][y] + g

    open = [[f, g, heuristic[x][y] , x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find distance
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            f = next[0]
            g = next[1]
            distance[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
    
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = heuristic[x2][y2] + g2
                            h2 = heuristic[x2][y2]
    
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            
                            
    c = distance[goal[0]][goal[1]]
    path = []
    path.append(goal)
    x = goal[0]
    y = goal[1]
    while c != 0:
        found = 0
        i = 0
        while (found == 0 and i < 4):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if distance[x2][y2] < c and distance[x2][y2] != -1:
                    found = 1
                    c = distance[x2][y2]
                    path.append([x2,y2])
                    x = x2
                    y = y2
            i = i + 1

    path.reverse()
    
    return (path)
    
print (search(grid,init,goal))