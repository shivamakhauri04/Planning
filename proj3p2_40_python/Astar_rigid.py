import pygame
import numpy as np
from sys import exit
import sys
import math

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        # define the properties of the node
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0


def heuristic(start, goal):
    # calculate distance between points
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    #return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    return math.sqrt(dx**2+dy**2)


def get_moves(step,theta) :
    # calculate the movement angles considering the orientations
    t1 = math.radians(theta)+math.pi/6
    t2 = math.radians(theta)+math.pi/3
    t3 = math.radians(theta)
    t4 = math.radians(theta) -math.pi/6
    t5 = math.radians(theta)- math.pi/3
    moves = [(math.cos(t1)*step, math.sin(t1)*step, 30),(math.cos(t2)*step, math.sin(t3)*step, 60), (math.cos(t3)*step, math.sin(t3)*step, 0) , (math.cos(t4)*step, math.sin(t4)*step, -30), (math.cos(t5)*step, math.sin(t5)*step, -60)]
    return moves

def astar(maze, start, end,distance,step):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    start_node.f = 0
    
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Make sure the robot does not revolve at its own place
    if start_node.position[2]> 360:
        start_node.position[2] = start_node.position[2]-360
    elif start_node.position[2]<0:
        start_node.position[2] = 360 - abs(start_node.position[2])
    # append start node in the visited list
    open_list.append(start_node)


    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node   Based on the f scores
        open_list.sort(key=lambda x: x.f,reverse=True)
        # Pop current off open list, add to closed list
        current_node = open_list.pop()
        
        
        # Found the goal
        #if (current_node.position == end_node.position):
        if (math.sqrt((current_node.position[0] - end_node.position[0])**2 +  (current_node.position[1] - end_node.position[1])**2 )<1.5):
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Return reversed path
            return path[::-1],closed_list, open_list 
        # Make sure the robot does not revolve at its own place
        if current_node.position[2]> 360:
            current_node.position[2] = current_node.position[2]-360
        elif current_node.position[2]<0:
            current_node.position[2] = 360 - abs(current_node.position[2])
        closed_list.append(current_node)
        
        # Generate children
        children = []
        for new_position in get_moves(step,current_node.position[2]):
            # Get node position
            node_position = [current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2]]

            # check within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if obstacle(node_position[0],node_position[1],distance) != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)
            new_node.g = current_node.g+1
            new_node.f = new_node.g + heuristic(end,new_node.position)

            # Append
            if new_node.position[2]> 360:
                    new_node.position[2] = new_node.position[2]-360
            elif new_node.position[2]<0:
                new_node.position[2] = 360 - abs(new_node.position[2])
            children.append(new_node)
        
        
        # Loop through children
        for neighbour in children:
            # chek if child in closed list
            if [int(neighbour.position[0]), int(neighbour.position[1]),
                neighbour.position[2]] in closed_list:
                continue

                
            temp = [[int(items.position[0]),int(items.position[1])] for items in open_list]
            # check if child in openset
            if [int(neighbour.position[0]),int(neighbour.position[1])] in temp:
                # Make sure the robot does not revolve at its own place
                if neighbour.position[2]> 360:
                    neighbour.position[2] = neighbour.position[2]-360
                elif neighbour.position[2]<0:
                    neighbour.position[2] = 360 - abs(neighbour.position[2])
                # swap child if present in openlist
                for i in range(len(open_list)):
                    if open_list[i].position == neighbour.position:
                        dis1 = heuristic(open_list[i].parent.position,start_node.position)
                        dis2 = heuristic(neighbour.parent.position,start_node.position)
                        if dis1> dis2:
                            open_list[i].parent = neighbour.parent
                            open_list[i].f = neighbour.f
            else:
                # Make sure the robot does not revolve at its own place
                if neighbour.position[2]> 360:
                    neighbour.position[2] = neighbour.position[2]-360
                elif neighbour.position[2]<0:
                    neighbour.position[2] = 360 - abs(neighbour.position[2])

                neighbour.parent = current_node
                open_list.append(neighbour)
                


        
            
            

def obstacle(x,y,distance):
        index = 0
        # circle
        if ((x-225)**2)+((y-150)**2)-((25+distance)**2)<=0:
            index=1
        #  ellipse200
        if ((x-150)/(40+distance))**2 + ((y - 100)/(20+distance))**2 - 1 <=0:
            index=1
        # quad
        if (y-(3/5)*(x+distance)+((475/5)-distance) <=0) and (y-(3/5)*(x-distance)+(625/5)+distance>=0) and  (y+(3/5)*(x+distance)-(725/5)+distance>=0)and  (y+(3/5)*(x-distance)-(875/5)-distance <=0):
            index=1
        # poly
        if (y-13*(x+distance)+140-distance <=0) and (y-185-distance <=0) and (y-(x-distance)-100+distance >=0) and (5*y-7*x-400 >=0) :
            index=1
        if (y+(7/5)*(x-distance)-(1450/5)-distance<=0) and (y-(6/5)*(x-distance)-(150/5)+distance>=0) and (y+(6/5)*(x+distance)-(1050/5)+distance>=0) and (y-(7/5)*x-(400/5) <=0):
            index = 1
        # rect
        if(y - 1.732*(x+distance) - 15.456864 -distance<=0) and (y + 0.577*(x-distance) - 96.382696 -distance<= 0) and (y- 1.732*(x-distance) + 134.54+distance >= 0) and (y + 0.577*(x+distance) - 84.815+distance >= 0):
            index = 1
        return index

def obstacle_plot(x,y):
        index = 0
        # circle
        if ((x-225)**2)+((y-150)**2)-(25**2)<=0:
            index=1
        #  ellipse200
        if ((x-150)/40)**2 + ((y - 100)/20)**2 - 1 <=0:
            index=1
        # quad
        if (5*y-3*x+475 <=0) and (5*y-3*x+625>=0) and  (5*y+3*x-725>=0)and  (5*y+3*x-875<=0):
            index=1
        # rect
        if (y-13*x+140 <=0) and (y-185 <=0) and (y-x-100 >=0) and (5*y-7*x-400 >=0) :
            index=1
        if (5*y+7*x-1450<=0) and (5*y-6*x-150>=0) and (5*y+6*x-1050>=0) and (5*y-7*x-400 <=0):
            index = 1
        # poly
        if(y - 1.732*x - 15.456864 <=0) and (y + 0.577*x - 96.382696 <= 0) and (y- 1.732*x + 134.54 >= 0) and (y + 0.577*x - 84.815 >= 0):
            index = 1
        return index

def plotPygame(new_endgoal,visited, openList):
        index = 4
        observation = []
        # read the obstacles and fill it in the pygame
        for i in range(0,301):
            for j in range(0,201):
                c=obstacle_plot(i,j)
                if c==1:
                    observation.append([i,j])
                    
        state=np.array(observation)
        observation=state*index

        path1 = np.array(new_endgoal)
        new_endgoal=path1*index
        pygame.init()
        # size of the pygame display
        size = [300*index, 200*index]
        display = pygame.display.set_mode(size)
        pygame.display.set_caption("A star Robot") 
        clock = pygame.time.Clock()
        done = False

        while not done:
            # fill the background
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:  
                    done = True 
            display.fill([0,0,0])
            # fill the obstacles
            for i in observation:
                pygame.draw.rect(display, [200,200,255], [i[0],200*index-i[1],index,index])
            for i in visited:
                pygame.draw.rect(display, [255, 255, 255], [i.position[0]*index, 200 * index - i.position[1]*index, index, index])
            for i in openList:
                pygame.draw.rect(display, [255, 255, 255], [i.position[0]*index, 200 * index - i.position[1]*index, index, index])
            # pygame.display.flip()
            clock.tick(20)
            # fill the traversed nodes will green
            '''
            for i in visited:
                pygame.time.wait(1)
                pygame.draw.rect(display, [0,255,0], [i[0],200*index-i[1],index,index])
                pygame.display.flip()
            '''
            # draw the shortest path in blue
            print (new_endgoal[:])
            for j in new_endgoal:
                pygame.time.wait(1)
                pygame.draw.rect(display, [255,0,0], [j[0], 200*index-j[1], index*2,index*2])
                pygame.display.flip()
            for i in range(len(new_endgoal)-3):
                points = [(new_endgoal[i][0],200*index-new_endgoal[i][1]),(new_endgoal[i+1][0],200*index-new_endgoal[i+1][1]),(new_endgoal[i+2][0],200*index-new_endgoal[i+2][1])]
                pygame.draw.polygon(display, (255, 0, 0), points)
                

            pygame.display.flip()
            temp = input()
            pygame.time.wait(15000)
            done = True
            
        pygame.quit()




def main():

    print("Enter robot parameters")
    radius=int(input("radius =  "))
    clearance=int(input("clearence =  "))
    distance  = radius+clearance
    print("Enter initial node cordinates")
    xi=int(input("x =  "))
    yi=int(input("y =  "))
    
    print("Enter goal node cordinates")
    xg=int(input("x =  "))
    yg=int(input("y =  "))
    
    step = float(input("Step Size (between 0.5 and 10) =  "))
    print (" Enter initial oritation")
    theta = int(input("angle= "))

    start = [xi, yi, theta]
    goal = (xg,yg)
    # create the map
    maze = [[0]*201 for i in range(301)]
    
    for i in range(301):
            for j in range(201):
                c=obstacle(i,j,distance)
                if c==1:
                    maze[i][j] = 1
    # check for obstacles
    if (obstacle(goal[0],goal[1],distance)==1 or obstacle(start[0],start[1],distance)):
        sys.exit("Either goal node or start node lies inside obstacle or outside the workspace")
    # run astar
    path,explored_nodes, openList = astar(maze, start, goal,distance,step)
    
    plotPygame(path,explored_nodes, openList)



if __name__ == '__main__':
    main()
