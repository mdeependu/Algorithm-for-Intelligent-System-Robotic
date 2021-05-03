class Node():
    def __init__(self, parent=None, position=None):
        self. parent = parent
        self. position = position
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self,other):
        return self.position == other.position


def A_Star (start, end, maze):
    openList = []
    closedList = []

    startNode = Node(None, start)
    startNode.f = startNode.g = startNode.h = 0

    endNode = Node(None, end)

    openList.append(startNode)
    
    while (len(openList)>0):  
        current_ = openList[0]
        current_index = 0
        children = []

        for index, item in enumerate(openList):
            if (item.f < current_.f):
                current_ = item
                current_index = index


        openList.pop(current_index)
        closedList.append(current_)


        if (current_==endNode):
            path = []
            curr = current_

            while curr is not None:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]


        for new_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nodePosition = (current_.position[0] + new_pos[0], current_.position[1] + new_pos[1])

            if nodePosition[0] > (len(maze)-1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
                continue

            if (maze[nodePosition[0]][nodePosition[1]]!=0):
                continue

            newNode = Node(current_, nodePosition)

            children.append(newNode)


            for child in children:
                for x in closedList:
                    if (child==x):
                        continue

            child.g = current_.g + 1
            child.h = ((child.position[0] - endNode.position[0])**2) + ((child.position[1] - endNode.position[1])**2)
            child.f = child.g + child.h

            for openNode in openList:
                if (child == openNode) and (child.g > openNode.g):
                    openList.append(child)


def MakePath (maze, path):

    for i in range(len (maze)):
        for j in range(len (maze)):
            if (i,j) in path:
                maze[i][j] = 3
    
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    start = (0,0)
    end = (9,6)
    
    print("A* Algorithm\n")
    
    path = A_Star (start,end,maze)
    
    print("The shortest path starting at position {} is:".format(start))
    print("Path: {}".format(path))
    
    MakePath (maze, path)
    for i in range(len(maze)):
        print(maze[i])

'''
print("A* Algorithm\n")
print("The shortest path starting at position (0, 0) is:")
print("Path: [(0 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 4), (6, 5), (7, 6), (8, 6), (9, 6)]")
'''