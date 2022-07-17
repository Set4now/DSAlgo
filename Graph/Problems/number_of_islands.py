# https://leetcode.com/problems/number-of-islands/
# https://www.youtube.com/watch?v=__98uL6wst8
def evluateisland(x, y, rows, cols, place):
    if ( x < 0 ) or ( x >= rows ) or ( y < 0 ) or ( y >= cols ) or ( place[x][y] != "1"):
        return 
    
       
    place[x][y] = "2" # making this land as a part of island

    # recursively call its top, down, left, right cell
    evluateisland(x - 1, y, rows, cols, place) # top 
    evluateisland(x + 1, y, rows, cols, place) # bottom
    evluateisland(x, y - 1, rows, cols, place) # left 
    evluateisland(x, y + 1, rows, cols, place) # right 

def numberofislands(place):
    
    rows = len(place)
    cols = len(place[0])
    
    count = 0
    for i in range(len(place)):
        for j in range(len(place[i])):
            # print(place[i][j])
            #print(i,j, place[i][j])
            if place[i][j] == "1":
                evluateisland(i, j, rows, cols, place)
                count += 1
    print(place)
    return count

#place = [[0,1,1,1,0,0,0]]
place = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numberofislands(place))


