from typing import List

"""

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.


Binary Search with memoization


"""

######### Normal Recursion ##########
# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         self.stones = stones
#         #print(max(stones))
#         #return self.possible(1, 1, max(self.stones))
#         return self.possible(1, 1,max(self.stones))

#     def possible(self, k, j, lastunit):
#         #print(k , j)
#         if k == lastunit:
#             return True
#         if k > lastunit or not self.search(self.stones, k):
#             return False

#         if  self.possible(k + j, j, lastunit):
#             return True

      
#         if  self.possible(k + j + 1, j + 1, lastunit):
#             return True

#         if k > 1 and j > 1:
#             if  self.possible(k + (j - 1), j - 1, lastunit):
#                 return True

#         return False

#     def search(self, arr, n):
#         #print(arr)
#         if not arr:
#             return False
#         mid = len(arr) // 2
#         if arr[mid] == n:
#             return True
#         if n < arr[mid]:
#             return self.search(arr[:mid], n)
#         if n > arr[mid]:
#             return self.search(arr[mid+1:], n)




############ DP with memoization ############
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.stones = stones
        dp = {}
        # i --> current jump unit, j --> last jump unit, initially they are both 1 as give in the question
        return self.possible(1, 1,max(self.stones), dp)

    def possible(self, k, j, lastunit, dp):
        # k is current unit, j is last jump unit

        if k == lastunit:
            dp[(k,j)] = True
            return dp[(k,j)]
        if k > lastunit or not self.search(self.stones, k):
            dp[(k,j)] = False
            return dp[(k,j)]

        if (k,j) in dp:
            return dp[(k,j)]
        else:
            # If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.

            # another jump of same k units
            if  self.possible(k + j, j, lastunit, dp):
                dp[(k,j)] = True
                return dp[(k,j)]

            # another jump of same k + 1 units
            if  self.possible(k + j + 1, j + 1, lastunit, dp):
                dp[(k,j)] = True
                return dp[(k,j)]

            # another jump of same k - 1 units from curren unit
            if k > 1 and j > 1:
                if self.possible(k + (j - 1), j - 1, lastunit, dp):
                    dp[(k,j)] = True
                    return  dp[(k,j)]
        dp[(k,j)] = False
        return  dp[(k,j)]


    

    def search(self, arr, n):
        #print(arr)
        if not arr:
            return False
        mid = len(arr) // 2
        if arr[mid] == n:
            return True
        if n < arr[mid]:
            return self.search(arr[:mid], n)
        if n > arr[mid]:
            return self.search(arr[mid+1:], n)





s = Solution()
stones = [0,1,3,5,6,8,12,17]

#stones = [0,1,2,3,4,5,6,7]
#stones = [0,1,3,8]
#stones = [0,1,3]

stones = [0,1,2,3,4,8,9,11]
#stones = [0,1,3,6,10,13,15,18]
print(s.canCross(stones))