"""

House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Parent problem
Find max subsequent sum from an array 

Slight variation in this problem
the subsequent should not have adjacent items
and consider the first and last element are adjacent


"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def max_subsequent_sum_without_adjacent(arr):
            prev = arr[0]
            prev2 = 0
            for i in range(1, len(arr)):
                pick = arr[i]
                if i > 1:
                    pick += prev2
                notpick = 0 + prev
                curr = max(pick, notpick)
                prev2 = prev
                prev = curr
            return prev
        
        array_excluding_last_index = nums[:-1]
        array_excluding_first_index = nums[1:]
        
        return max(
            max_subsequent_sum_without_adjacent(array_excluding_last_index),
            max_subsequent_sum_without_adjacent(array_excluding_first_index)
        
        )