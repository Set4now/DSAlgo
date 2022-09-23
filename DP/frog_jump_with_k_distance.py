"""
Follow up Question from min energy required by the from to go from 0 to (n - 1) stairs
where if frog is at ith position, he is allowed to jump from i to i+1 stair and i to i+2 stair
and engery consumed in a jump  from i to j is height[j] - height[i]

Now, find out if a frog is allowed to jump k distance
means
k + 1,k+2...k + n
"""


# TIme complexity is N * K
#  SC  O(N) + O(N) , extra O(N ) if we apply memoization
def min_enery_k_distance(height, k):

    def helper(index, n, height, k):
        if height[index] == n:
            return 0
        temp = float("Inf")
        for i in range(1, k+1):
            if index + i < n + 1:# n + 1 is length of height, should not outbound the length of  array
                enery = helper(index + i) + abs(height[index+i] - height[index])
                if enery < temp:
                    temp = enery
        return temp

    last_index = len(height) - 1
    return helper(0, last_index, height, k)

# Space optimization with variables ( Not using Dp array)
# But this is not required since if k is equal to N , then again the space would be same as DP array 
def min_energy(height, k):
    ans = [0] * k
    for index in range(1, len(height)):
        temp = float("inf")
        for j in range(k):
            if index - j > 1:
                energy = ans[j] + abs(height[index - j]- height[index])
                temp = min(temp, energy)
        ans.pop()
        ans.insert(0, temp)
    return ans[0]
    
    

