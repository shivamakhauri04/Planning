#Pseudocode
# Input the initial matrix
# Input the goal matrix
# Create a graph node with the initial input matrix
# Calculate the f score of the start node
# Expand the current node and append the expanded matrces each as a node to the graph in the Open list
# Push the current node into closed list
# Calculate the fsore again for each node
# State with the least fscore is expanded again
# Continue the above process till the current_state=goal_matrix


class GraphNode:
    def __init__(self,data,level,fvalue):
        self.data = data
        self.level = level
        self.fvalue = fvalue 
    
    

class Astar:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def inputMatrix(self):
        data = []
        for i  in range(self.n):
            row = input().split(" ")
            data.append(row)
        return data

    def f_score(self,start,goal):
        return self.h_score(start.data,goal)+start.level
    
    def h_score(self,start,goal):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != "_":
                    temp +=1
        return temp

    def main(self):
        print("input the start matrix(3*3)- Enter the data rowwise with spaces in between elements")
        initialMatrix = self.inputMatrix()
        print("input the goal matrix(3*3)- Enter the data rowwise with spaces in between elements")
        goalMatrix = self.inputMatrix()
        initialMatrix = GraphNode(initialMatrix,0,0)
        initialMatrix.fvalue = self.f_score(initialMatrix,goalMatrix)
        self.open.append(initialMatrix)
        # Creating recursion
        while True:
            current_matrix = self.open[0]
            print("")
            print("######################")
            for i in current_matrix.data:
                for j in i:
                    print(j)
                print("")
        # limiting condition for recursion so that doesn't run infinitely
        if(self.h_score(current_matrix.data,goal)==0):
            break
        





puzzle = Astar(3)
puzzle.main()