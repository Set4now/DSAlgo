"""
https://leetcode.com/problems/house-robber/submissions/


There is unsorted integer array, return a maximum sum of non adjacent elements.

example>
[5, 20, 15, -2, 18] => 20 + 18 = 38
[4, 1, 6, 3, 2] => 4 + 6 + 2 = 12

I never seen this problem in leetcode, anybody pls let me know how to approach this.

I googled it and the solution seems different when the negative number exists or not.





Solution:
Modified version of print all subsequences

"""

from typing import List


def sum_subsquences(index, arr):
    if index == len(arr) - 1: 
        return arr[index]
    if index >= len(arr):
        #result.append([i for i in output])
        return 0

    #pick the index
    pick = None
    #if index + 2 < len(arr):
    pick = arr[index] + sum_subsquences(index+2, arr)

    # don't pick the index
    notpick = None
    #if index + 1 < len(arr):
    notpick = 0 + sum_subsquences(index+1, arr)
    if pick is not None and notpick is not None:
        return max(pick, notpick)
    if notpick is None and pick:
        return pick
    if pick is None and notpick:
        return notpick
    #sum_subsquences(index + 1, arr)
    #return pick
    #print_subsquences(index + 1, arr, output)

# arr = [1,2,3,4,5,6,7,8,9]
# arr = [4, 1, 6, 3, 2]
# arr = [5, 20, 15, -2, 18]
# arr=[0,0]
# print(sum_subsquences(0, arr))


###### DP with mempization, rob house 1 leetcode
class Solution:
    def rob(self, nums: List[int]) -> int:
        def sum_subsequence_not_adjacenthouse(index, nums, dp):
            if index == len(nums) - 1:
                dp[index] = nums[index]
                return dp[index]
            if index >= len(nums):
                return 0
            
            if dp[index] != -1:
                return dp[index]
            else:
                pick = nums[index] + sum_subsequence_not_adjacenthouse(index+2, nums, dp)
                
                notpick = 0 + sum_subsequence_not_adjacenthouse(index+1, nums, dp)
                dp[index] = max(pick, notpick)
                return dp[index]

                
        dp = [-1] * ( len(nums) + 1 )
        return sum_subsequence_not_adjacenthouse(0, nums, dp)


arr = [1,2,3,4,5,6,7,8,9]
arr = [4, 1, 6, 3, 2]
arr = [5, 20, 15, -2, 18]
#arr=[0,0]
s = Solution()
print(s.rob(arr))


###### Tabular Bottom up ########

class Solution:
    def rob(self, nums: List[int]) -> int:

        # changing the Memoization to tabular, removing recusuon stack    
        n = len(nums)     
        dp = [-1] * n
        dp[0] = nums[0]
        for i in range(1, n):
            pick = None
            if i - 2 >= 0:
                pick = nums[i] + dp[i - 2]
            else:
                pick = nums[i]

            notpick = None
            if i - 1 >= 0:
                notpick = 0 + dp[i - 1]
            else:
                notpick = nums[i]
 
            if pick is not None and notpick is not None:
                dp[i] = max(pick, notpick)
            if pick is not None and notpick is None:
                dp[i] = pick
            if notpick is not None and pick is None:
                dp[i] = notpick

        return dp[n-1]

#arr = [1,2,3,4,5,6,7,8,9]
#arr = [4, 1, 6, 3, 2]
#arr = [5, 20, 15, -2, 18]
#arr=[0,0]
#arr = [1,2]
#s = Solution()
#print(s.rob(arr))    


# Space Optimizarion with TC - O(N), SC - O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge for inputs with just 1 item 
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        prev2 = nums[1]
        for i in range(1, len(nums)):
            pick = None
            if i - 2 >= 0:
                pick = nums[i] + prev2
            else:
                pick = nums[i]
            notpick = None
            if i - 1 >= 0:
                notpick = 0 + prev
            else:
                notpick = nums[i]
            
            
            if pick is not None and notpick is not None:
                curr = max(pick, notpick)
            if pick is not None and notpick is None:
                curr = pick
            if notpick is not None and pick is None:
                curr = notpick

            prev2 = prev
            prev = curr
        return prev


#arr = [1,2,3,4,5,6,7,8,9]
#arr = [4, 1, 6, 3, 2]
# arr = [5, 20, 15, -2, 18]
# arr=[0,0]
# #arr = [1,2]
# s = Solution()
# print(s.rob(arr))    