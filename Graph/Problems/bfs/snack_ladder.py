from typing import List

# class QueueEntry(object):
#     def __init__(self, v=0, dist=0):
#         self.v = v
#         self.dist = dist

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cellqueue = []
        #throw = 0
        visited = set()

        n = len(board)
        target = len(board) * len(board)
        

        #starting point (cell 0 , throw 0) which is basically cell 0,col 0 of n - 1 row,
        # since we play the game from bottom left corner
        distance = 0
        cellqueue.append((0, distance)) 
        board.reverse()


        # Ideally you can visualise it as an one D array
        # where each index is the cell number
        oneDarray = []
        for i in range(n):
            if i % 2 == 0:
                oneDarray.extend(board[i])
            else:
                oneDarray.extend(board[i][::-1])
        
        while cellqueue:
            print(cellqueue)
            # print(visited)
            # print("=====")
            cell, distance = cellqueue[0]
            del cellqueue[0]

            

            for i in range(1, 7):
                nextcell = cell + i 
                if nextcell == target - 1:
                    return distance
                # print(nextcell)
                if nextcell < target:
                # nextcell = oneDarray[cell + i]
                    if oneDarray[nextcell] != -1:
                        nextcell = oneDarray[nextcell]
                        
                        # oneDarray[nextcell] = oneDarray[nextcell]
                    if nextcell not in visited:
                        visited.add(nextcell)
                        cellqueue.append((nextcell, distance + 1))
        # if distance:
        #     return distance

        return -1



"""
[
 -1, 15, -1, -1, -1, -1,
 -1, -1, -1, -1, -1, -1, 
 -1, 35, -1, -1, 13, -1, 
 -1, -1, -1, -1, -1, -1, 
 -1, -1, -1, -1, -1, -1, 
 -1, -1, -1, -1, -1, -1
 ]


"""
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

#board = [[-1,-1],[-1,3]]
s = Solution()
print(s.snakesAndLadders(board))
                




