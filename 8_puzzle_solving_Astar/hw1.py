#Pseudocode
# Input the initial matrix
# Input the goal matrix
# Create a graph node with the input
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
    def main(self):


puzzle = Astar()
puzzle.process()