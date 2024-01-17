from queue import Queue

'''Find one of the shortest paths from the start node to the end node in the grid, while avoiding the obstacles. If no path is found then output [].
If a path is found add the coordinates of the path to the list and return it.
Recommended for everyone to do and understand this question, as it is a good introduction to BFS.'''
def findPath(grid):
    return []; # Replace this with your implementation


'''return all possible shortest paths from the start node to the end node in the grid.
return format is a list of lists of tuples. Each list of tuples is a shortest path, and each such path should be distinct.
Recommended to try if you have completed the previous question.'''
def findAllShortestPaths(grid):
    return []; # Replace this with your implementation


##You can use this below code to check if your implementation is correct.
def checkPath(path, grid, pathLength):
    if(pathLength != len(path)):
        return False; 
    if(len(path) == 0): return True;
    #else we need to check something else, that the path is valid or not, and does it end at the end position.
    if(grid[path[0][0]][path[0][1]] != 'S'): return False; 
    if(grid[path[-1][0]][path[-1][1]] != 'E'): return False; 
    for i in range(len(path) - 1):
        if(path[i][0] >= len(grid) or path[i][1] >= len(grid[0])): return False; 
        if(path[i][0] < 0 or path[i][1] < 0): return False; 
        if(grid[path[i][0]][path[i][1]] == '#'): return False; 
        if(abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) != 1): return False;
    return True;

### CAUTION IF EDITING THE CODE BELOW THIS LINE ###
#helps to take the input and output the answer. IF you would like to test your code, this is the best way.
#Remember to not let any stray print statements in your code before the final submission, unless it is in main, as main will only be called locally and not when imported.
def main(): 
    grid = [];
    n = int(input()); #the size of the square grid.
    for i in range(n):
        grid.append(input().strip()); 
    path = findPath(grid); 
    print(path); 

if __name__ == '__main__':
    main(); 
    



