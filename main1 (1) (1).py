
def isPath(matrix, n):
    visited = [[False for x in range(n)] for y in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] == 1 and not visited[i][j]):
                if (checkPath(matrix, i, j, visited)):
                    flag = True
                    break
    print("\b\b\b\n Destination Reached")

def isSafe(i, j, matrix):
    if (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
        return True
    return False

oi=3
oj=3

def checkPath(matrix, i, j, visited):
    if (isSafe(i, j, matrix) and matrix[i][j] != 0 and not visited[i][j]):
        visited[i][j] = True
        global oi, oj

        #print("NEW " + str(i) + ", " + str(j))
        if(oi<i):
            print("DOWN -> ",end="")
        if(oj>j):
            print("LEFT -> ", end="")
        if (oi > i):
            print("UP -> ", end="")
        if (oj < j):
            print("RIGHT -> ", end="")
        oi = i
        oj = j

        if(matrix[i][j] == 2):
            return True

        # traverse up
        up = checkPath(matrix, i - 1, j, visited)
        # If path is found in up
        # direction return true
        if (up):
            return True

        # Traverse left
        left = checkPath(matrix, i, j - 1, visited)
        # If path is found in left
        # direction return true
        if (left):
            return True

        # Traverse down
        down = checkPath(matrix, i + 1, j, visited)
        # If path is found in down
        # direction return true
        if (down):
            return True

        # Traverse right
        right = checkPath(matrix, i, j + 1, visited)
        # If path is found in right
        # direction return true
        if (right):
            return True

    # No path has been found
    return False


# Driver code
if __name__ == "__main__":
    matrix = [[2, 3, 0, 0],
              [3, 3, 3, 3],
              [0, 0, 3, 3],
              [0, 0, 3, 1]]

    # calling isPath method
    isPath(matrix, 4)

    matrix = [[" D ", "   ", " \U0001F4A3 ", " \U0001F4A3 "],
              ["   ", "   ", "    ", "   "],
              [" \U0001F4A3 ", " \U0001F4A3 ", "   ", "   "],
              [" \U0001F4A3 ", " \U0001F4A3 ", "   ", " S "]]

    for i in matrix:
        for j in i:
            print("|"+j,end="")
        print("|")