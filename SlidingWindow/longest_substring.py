"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "acbcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Solution:
Using Sliding Window

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        i = 0
        j = 1
        ans = -float("Inf")
        curr = s[i]
        while  j < len(s) and i < len(s):
            # if non repeating character , add it to substring
            if s[j] not in curr:
                curr += s[j]
                j += 1
            else:
                # Repeating character found
                # Saving the current length of substring without the current repeating character
                ans = max(ans, len(curr))

                # removing all characters from current substring including the repeating charac
                # stop at the index of repeating one
                # increment i to i + 1
                delcounter = 1
                while i < j:
                    temp = curr
                    if s[i] == s[j]:
                        temp = temp[delcounter:]
                        i += 1
                        break
                    else:
                        temp = temp[delcounter:]
                        delcounter += 1
                        i  += 1
                # after removing, now add the current character
                # This means this is now our new substring without any repeating chars
                temp += s[j]
                curr = temp
                j += 1
        
        # Edee case if the initial complete string itself doesn't have any duplicate 
        # means we never encounteres the else cause, then return whatever is the length of curr
        ans = max(ans, len(curr))      
        return ans if ans != -float("Inf") else len(curr)
    
s = Solution()
s1 = "abcabcbb"
# s1 = "pwwkew"
s1 = "bbbbb"
s1 = ""
s1 = "au"
#s1 = "aab"
s1 = "dvdf"
print(s.lengthOfLongestSubstring(s1))

# curr = "acfrgdvd"
# i = 0
# j = len(curr) - 1
# count = 1
# while i < j:
#     print(i,j)
#     if curr[i] == curr[j]:
#         curr = curr[count:]
#         i += 1
#         break
#     else:
#         curr = curr[count:]
#         count += 1
#         i  += 1
#     j = len(curr) - 1
# print(curr)
      

    
    
