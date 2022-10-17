from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        group_one = defaultdict(list)
        group_two = defaultdict(list)

        output = 0

        for idxi, i in enumerate(nums1):
            for idxj, j in enumerate(nums2):
                t1 = i + j
                group_one[t1].append([idxi, idxj])

        for idxi, i in enumerate(nums3):
            for idxj, j in enumerate(nums4):
                t2 = i + j
                group_two[t2].append([idxi, idxj])

        
        print(group_one)
        print(group_two)

        for t1 in group_one:
            target = 0 - t1
            if target in group_two:
                # if len(group_one[t1]) > 1:
                #     output += ( len(group_one[t1])  + len(group_two[target]) )
                # elif len(group_one[t1]) == 1:
                #     output += len(group_two[target])
                output += len(group_two[target]) * len(group_one[t1])

        return output

nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]


nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

s = Solution()
print(s.fourSumCount(nums1, nums2, nums3, nums4))