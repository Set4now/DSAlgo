from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     multiplication_from_left = [nums[0]]
    #     for i in range(1, n):
    #         multiplication_from_left.append(multiplication_from_left[i-1] * nums[i])

    #     multiplication_from_right = [nums[n-1]]
    #     rev = nums[::-1]
    #     for i in range(1, n):
    #         multiplication_from_right.append(multiplication_from_right[i-1] * rev[i])


    #     multiplication_from_right = multiplication_from_right[::-1]
    #     #print(multiplication_from_left)
    #     #print(multiplication_from_right)

    #     output = [multiplication_from_right[1]]
    #     # output[0] = nums[0]
    #     for i in range(1, n-1):
    #         output.append(multiplication_from_left[i-1] * multiplication_from_right[i+1])
    #     output.append(multiplication_from_left[n-2])
    #     return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [nums[0]]
        for i in range(1, n):
            output.append(output[i-1] * nums[i])

        right_product = 1
        i = len(nums) - 1
        while i > 0:#
            curr = nums[i]
            output[i] = output[i-1] * right_product
            right_product *= curr
            i -= 1
        output[0] = right_product
        return output
    

nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
s = Solution()
print(s.productExceptSelf(nums))