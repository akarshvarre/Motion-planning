import numpy as np

max_step_num = 16

import numpy as np
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]
        
x = len(grid)
y = len(grid[0])

max_step_num = 16
delta = [[-1,0],[1,0],[0,1],[0,-1]]
init = [2,0]
goal = [x-1, y-1]

def search (world_state, robot_pose, goal_pose):

    max_step_num = 16
    prev_steps = []
    path = []
    curr_pose = robot_pose
    n = int (max_step_num**(0.5))
    path.append([curr_pose[0],curr_pose[1]])

    while (curr_pose != goal_pose and max_step_num > 0):
      
        not_valid = 1
        found = 0
        steps = [[-1,0],[1,0],[0,1],[0,-1]]
        num = len(steps)
        x2 = curr_pose[0]
        y2 = curr_pose[1]
        
        found_adj_steps = []
        while((not_valid == 1 or found == 1) and num > 0):
            found = 0
            not_valid = 1
            rnd_num = np.random.randint(num)

            num = num -1
            x2 = curr_pose[0] + steps[rnd_num][0]
            y2 = curr_pose[1] + steps[rnd_num][1]
            
            del steps[rnd_num]
            
            # check whether the next pose is inside the grid
            if x2>= 0 and x2< len(grid) and y2>= 0 and y2< len(grid[0]):
                # check whether the next pose is not the wall
                if world_state[x2][y2] != 1:
                    not_valid = 0
                    
                    # check if this is the first step
                    if (len(prev_steps) == 0):
                        break
                    # if not check if the next step is one of the prev steps
                    else:
                        for j in range(len(prev_steps)):
                            if x2 == prev_steps[j][1] and y2 == prev_steps[j][2] and prev_steps[j][0] != 0:
                                found = 1
                                found_adj_steps.append(prev_steps[j])
            
        # The next step is not found in the previous steps and 
        #it's a valid pose, then move to that pose                
        if found == 0 and not_valid == 0:
            
            prev_steps.append([n+1, curr_pose[0], curr_pose[1]])
            
            max_step_num = max_step_num - 1
            path.append([x2, y2])
            for j in range(len(prev_steps)):
                if prev_steps[j][0] > 0:
                  prev_steps[j][0] -= 1
            curr_pose[0] = x2
            curr_pose[1] = y2
            
        
        # all directions checked and if it does not have a choice, it goes to one of the previous steps
        elif len(found_adj_steps) != 0 and num == 0:
            found_adj_steps.sort()
            next = found_adj_steps.pop(0)
            path.append([next[1], next[2]])
            
            prev_steps.append([n, curr_pose[0], curr_pose[1]])
            max_step_num = max_step_num - 1
            for j in range(len(prev_steps)):
                if prev_steps[j][0] > 0:
                  prev_steps[j][0] -= 1
            curr_pose[0] = next[1]
            curr_pose[1] = next[2]
            
		# IF no way to go, return FAIL
        elif not_valid == 1 and num == 0:
            return ("FAIL")
            
        if len(prev_steps) > n:
            del prev_steps[:len(prev_steps)-n]
            
    if (curr_pose == goal_pose):
        print ("PASS")
        return (path)
    else:
        print ("FAIL")
        return (path)
    
print (search(grid,init,goal))