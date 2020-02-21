# class to store graph data
class GraphNode:
    # constructor
    def __init__(self,data,level,visited):
        # store the data of the node
        self.data = data
        # store the level of the graph
        self.level = level
        # track if the node is visited
        self.visited = visited 
    
    def find_zero(self,matrix,x):
        # find and return the index of zeros in the 2d array
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if matrix[i][j]==x:
                    return i,j
    
    def shift_graphElements(self,matrix,x1,y1,x2,y2):
        # generate new puzzle childrens by shifting the position of zero
        if x2 >=0 and x2 < len(self.data) and y2 >= 0 and y2 <len(self.data):
            temp_matrix = []
            # copy the original matrix in buffer to keep track
            temp_matrix = self.matrix_copy(matrix)
            # swap the elements to create new graph
            temp =  temp_matrix[x2][y2]
            temp_matrix[x2][y2] = temp_matrix[x1][y1]
            temp_matrix[x1][y1] = temp
            return temp_matrix
        else:
            None

    
    def expand_matrix(self):
        # to keep of track of the child
        child_tag = 0
        # to keep a track of the parent
        cnt = 0
        # call the function to find position of zero
        x,y = self.find_zero(self.data,0)
        parent_list = []
        parent_tag = 3*x + y
        parent_list.append(parent_tag)
        length = len(parent_list)
        # to track if a new parent is created
        parent_tag = set(parent_list)
        if len(parent_tag) != length:
            cnt = cnt +1
        # shuffle the puzzle to create new children
        shuffle_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        child_matrix = []
        f2 = open("NodesInfo.txt",'w')
        f = open('Nodes.txt','w')
        for i in shuffle_list:
            # for each children add the values in the text file
            child = self.shift_graphElements(self.data,x,y,i[0],i[1])
            child_tag = child_tag+1
            f2.write(str(child_tag))
            f2.write(' ')
            f2.write(str(cnt))
            f2.write('\n')
            if child is not None:
                # for each children store its data 
                buffer = []
                child_node = GraphNode(child,self.level+1,0)
                child_matrix.append(child_node)
                for m in child_node.data:
                    for n in m:
                        f.write(str(n))
                        f.write(' ')
                f.write('\n')
                print (buffer)       
                
                
        f2.close()       
        f.close()
        return child_matrix

    def matrix_copy(self,data):
        # create a copy of the matrix of the graph to keep its track before shuffling
        temp = []
        for i in data:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
    
    

class dfs:
    def __init__(self,size):
        # find the size of the row of the adjency matrix of the graph
        self.n = size
        # to keep a track of the unvisited nodes
        self.open = []
        # to keep a trcak of the visited nodes
        self.closed = []

    def inputMatrix(self):
        # input the elements of the puzzle from the user
        matrix = []
        for i in range(3):
            data = []
            for j in range(3):
                data.append(int(input()))
            matrix.append(data)
        return matrix
        

    def invCount(self,initialMatrix):
        # function to count the number of inversions 
        invCount = 0
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if initialMatrix[j]>initialMatrix[i]:
                    invCount = invCount + 1
        return invCount

    def checkSolvability(self,initialMatrix):
        # function to check if the number of inversions is odd
        temp = initialMatrix
        invCount = self.invCount(temp)
        return (invCount%2)


    def check_visited(self,start,goal):
        # function to keep a track of the visted nodes
        return self.visited_status(start.data,goal)+start.level
    
    def visited_status(self,start,goal):
        temp = 0
        # function to check the status of the graph node is visited
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp +=1
        return temp




def main():
    # constructor call
    DFS = dfs(3)
    print("input the start matrix(3*3)- Enter the data element by element")
    # add the input elements of the graph
    initialMatrix = DFS.inputMatrix()
    # check for solvability of the puzzle
    if (DFS.checkSolvability(initialMatrix)):
        print ("Not solvable")
    else:
        print("input the goal matrix(3*3)- Enter the data element by element")
        # if solvable, enter the goal matrix
        goalMatrix = DFS.inputMatrix()
        # traverse through the nodes of the matrix
        initialMatrix = GraphNode(initialMatrix,0,0)
        # track the nodes which have already been traversed
        initialMatrix.visited = DFS.check_visited(initialMatrix,goalMatrix)
        # store thepossible paths
        DFS.open.append(initialMatrix)
        print ('\n \n')
        # Creating recursion
        f1 = open("nodePath.txt","w")
        while True:
            current_matrix = DFS.open[0]
            print("")
            print("######################")
            print("\n")
            # store the graph cnfiguration for the best path
            for i in current_matrix.data:
                for j in i:
                    print(j,end = " ")
                    f1.write(str(j))
                    f1.write(' ')
   
                print("")
            f1.write('\n')  
            # limiting condition for recursion so that doesn't run infinitely
            if(DFS.visited_status(current_matrix.data,goalMatrix)==0):
                break
            for i in current_matrix.expand_matrix():
                # traverse the neighbours of the visited noeds to check if visited
                i.visited = DFS.check_visited(i,goalMatrix)
                DFS.open.append(i)
            # if noed travered, store it in closed list
            DFS.closed.append(current_matrix)
            del DFS.open[0]
            DFS.open.sort(key = lambda x:x.visited,reverse=False)
        f1.close()


main()
