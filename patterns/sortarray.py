from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        # print(i)
        while i >= 0:
            if nums1[i] == 0:
                nums1.pop()
            i -= 1
        # print(nums1)
        nums1.extend(nums2)
        nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


nums1 = [1]
m = 1
nums2 = []
n = 0

nums1 = [0]
m = 0
nums2 = [1]
n = 1

s = Solution()
print(s.merge(nums1, m, nums2, n))
print(nums1)

