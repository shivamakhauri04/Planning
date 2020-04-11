
import pygame
import numpy as np
from sys import exit
import sys
import math
import time
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, action = None):
        self.parent = parent
        self.position = position
        self.action = action

        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(start, goal):
    # calculate distance between points
    dx = abs(start[0] - goal[0])
    dy = abs(start[1] - goal[1])
    #return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    return math.sqrt(dx**2+dy**2)


def get_moves(theta,lw,rw) :
    # calculate the movement angles considering the orientations
    moves = [[0,lw],[lw,0],[lw,lw],[0,rw],[rw,0],[rw,rw],[lw,rw],[rw,lw]]
    return moves

def trajectory(X0,Y0,Theta0,UL,UR,distance):
    #print("here*****************************************************************")
    t = 0
    #r = 0.038
    r = 0.038
    L = 0.354
    dt = 0.1
    Theta0 = 3.14 * Theta0 / 180
    flag = 0
    while t<1:
        t = t + dt
        X1 = X0
        Y1 = Y0
        X0 += 0.5 *r * (UL + UR) * math.cos(Theta0) * dt 
        Y0 += 0.5 *r * (UL + UR) * math.sin(Theta0) * dt 
        Theta0 += (r/L) * (UR - UL) * dt 
        #print(X0,Y0,distance)

        #plt.plot([X0, X1], [Y0, Y1], color="blue")
        if obstacle_test(X0,Y0,distance)!=0:
            flag =1

    Theta0 = 180 * (Theta0) / 3.14
    #points.append()
    return [X0, Y0, Theta0],flag


def trajectory_plot(X0,Y0,Theta0,UL,UR):

    t = 0
    r = 0.038
    L = 0.354
    dt = 0.01
    Theta0 = 3.14 * Theta0 / 180
    x_list = []
    y_list = []
    theta_list = []
    while t<1:
        t = t + dt
        X1 = X0
        Y1 = Y0
        X0 += (0.5)*r* (UL + UR) * math.cos(Theta0) * dt
        Y0 += (0.5)*r * (UL + UR) * math.sin(Theta0) * dt
        Theta0 += (r/L) * (UR - UL) * dt
        #print(X0,Y0)
        x_list.append(X0)
        y_list.append(Y0)
        theta_list.append(Theta0)
        #plt.plot([X0, X1], [Y0, Y1], color="blue")

    Theta0 = 180 * (Theta0) / 3.14
    #points.append()
    return [x_list,y_list, theta_list]



def astar(maze, start, end,distance, lw, rw):
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
    # Add the start node
    open_list.append(start_node)


    # Loop until you find the end
    while len(open_list) > 0:
        print ("##### Exploring #####")

        # Get the current node   Based on the f scores
        open_list.sort(key=lambda x: x.f,reverse=True)
        # Pop current off open list, add to closed list
        current_node = open_list.pop()
        #print(current_node.position)
        
        # Found the goal
        #if (current_node.position == end_node.position):
        if (math.sqrt((current_node.position[0] - end_node.position[0])**2 +  (current_node.position[1] - end_node.position[1])**2 )<0.5):
            path = []
            actions = []
            current = current_node
            while current is not None:
                path.append(current.position)
                actions.append(current.action)
                current = current.parent

            # Return reversed path
            return path[::-1],closed_list, open_list, actions[::-1]



        # Make sure the robot does not revolve at its own place
        if current_node.position[2]> 360:
            current_node.position[2] = current_node.position[2]-360
        elif current_node.position[2]<0:
            current_node.position[2] = 360 - abs(current_node.position[2])
        closed_list.append(current_node)
        
        # Generate children
        children = []
        for new_position in get_moves(current_node.position[2],lw,rw):
            
            # Get node position

            node_position, flag = trajectory(current_node.position[0],current_node.position[1],current_node.position[2],new_position[0],new_position[1],distance)
            if flag==1:
                continue

            # print (node_position)
            # check within range
            if node_position[0] > 10 or node_position[0] < 0 or node_position[1] > 10 or node_position[1] < 0:
                continue


            #if obstacle_test(tempx,tempy,distance) != 0:
            #    continue

            # Create new node
            new_node = Node(current_node, node_position)
            new_node.g = current_node.g+1
            new_node.f = new_node.g + heuristic(end,new_node.position)
            new_node.action = new_position
            # Append
            if new_node.position[2]> 360:
                    new_node.position[2] = new_node.position[2]-360
            elif new_node.position[2]<0:
                new_node.position[2] = 360 - abs(new_node.position[2])
            children.append(new_node)
        
        
        # Loop through children
        for neighbour in children:
            
           
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
                

def obstacle_test(x,y,distance):
    index = 0
    # #Top left square
    if(y-(5.75+distance)<=0) and (y-(4.25-distance)>=0)  and (x-(1.5+distance)<=0) and (x-(0.25-distance)>=0):
        index=1
    #Middle right square
    if (y-(8.75+distance)<=0) and (y-(7.25-distance)>=0) and (x-(2.25-distance)>=0) and (x-(3.75+distance)<=0):
        index=1
    #Middle Left square
    if(y-(5.75+distance)<=0) and (y-(4.25-distance)>=0) and (x-(8.25-distance)>=0) and (x-(9.75+distance)<=0):
        index = 1
    #Centre Circle
    if(((x-5)**2)+((y-5)**2)-((1+distance)**2))<=0:
        index = 1
    #Upper right circle
    if(((x-7)**2))+((y-8)**2)-((1+distance)**2)<=0:
        index = 1
    #Lower right circle
    if(((x-7)**2))+((y-2)**2)-((1+distance)**2)<=0:
        index = 1
    #Lower left circle
    if(((x-3)**2))+((y-2)**2)-((1+distance)**2)<=0:
        index = 1
    return index
        
            
            

def obstacle(x,y,distance):
    index = 0
    # #Top left square
    if(y-(3.75+distance)<=0) and (y-(2.25-distance)>=0) and (x+(2.75+distance)>=0) and (x+(1.25-distance)<=0):
        index=1
    #Middle right square
    #if(y-3.75+distance<=0) and (y+(2.75+distance)>=0) and (x-(2.25-distance)>=0) and (x-(1.25-distance)<=0):
    #    index=1
    if(y-(0.75+distance)<=0) and (y+(0.75+distance)>=0) and (x-(3.25-distance)>=0) and (x-(4.75+distance)<=0):
        index=1
    #Middle Left square
    if(y-(0.75+distance)<=0) and (y+(0.75+distance)>=0)  and (x+(3.25-distance)<=0) and (x+(4.75+distance)>=0):
        index = 1
    #Centre Circle
    if((x**2)+(y**2)-(1+distance))<=0:
        index = 1
    #Upper right circle
    if((x-2)**2)+((y-3)**2)-(1+distance)<=0:
        index = 1
    #Lower right circle
    if((((x-2)**2))+((y+3)**2)-(1+distance))<=0:
        index = 1
    #Lower left circle
    if(((x+2)**2))+((y+3)**2)-(1+distance)<=0:
        index = 1

    return index

def obstacle_plot(x,y):
    index = 0
    # #Top left square
    if(y-(3.75)<=0) and (y-(2.25)>=0) and (x+(2.75)>=0) and (x+(1.25)<=0):
        index=1
    #Middle right square
    if(y-0.75<=0) and (y+0.75>=0) and (x-3.25>=0) and (x-4.75<=0):
        index=1
    #Middle Left square
    if(y-0.75<=0) and (y+0.75>=0)  and (x+3.25<=0) and (x+4.75>=0):
        index = 1
    #Centre Circle
    if((x**2)+(y**2)-1)<=0:
        index = 1
    #Upper right circle
    if((x-2)**2)+((y-3)**2)-1<=0:
        index = 1
    #Lower right circle
    if((((x-2)**2))+((y+3)**2)-1)<=0:
        index = 1
    #Lower left circle
    if(((x+2)**2))+((y+3)**2)-1<=0:
        index = 1

    return index



def main(myargv):

    print("Enter robot parameters")
    radius= 0.038
    clearance= 0.0
    distance  = radius+clearance
    print("Enter initial node cordinates")
    
    xi= int(myargv[1])
    yi= int(myargv[2])
    theta = 0
    
    print("Enter goal node cordinates")
    xg= int(myargv[3])
    yg= int(myargv[4])
    
    #step = int(input("Step Size (between 1 and 10) =  "))
    
    print ("wheel RPM's")
    lw = int(myargv[5])
    rw = int(myargv[6])



    start = [xi, yi, theta]
    goal = (xg,yg)

    maze = [[0]*100 for i in range(100)]
    
    for i in range(0,100,1):
        for j in range(0,100,1):
            c = obstacle(i/10-5,j/10-5,distance)
            if c != 1:
                maze[i][j] = 1
                #plt.scatter(i,j,c=maze[i,j],s=100,cmap='hot',marker='s')
    #print (maze[0][-3])
    arr = np.array(maze)
    x,y = arr.nonzero()
                    
    
    if (obstacle(goal[0],goal[1],distance)==1 ):
        sys.exit("Goal node in obstacle")
    if (obstacle(start[0],start[1],distance)==1 ):
        sys.exit("Goal node in obstacle")

    start = [xi+5, yi+5, theta]
    goal = (xg+5,yg+5)
        
    begin = time.time()
    path,explored_nodes, openList, actions = astar(maze, start, goal,distance, lw, rw)
    print (actions)
    end = time.time()
    print (end-begin)
    return(actions)




if __name__ == '__main__':
    main()
