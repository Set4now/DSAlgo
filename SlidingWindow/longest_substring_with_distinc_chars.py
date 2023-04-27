
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == len(set(s)):
            return len(s)
        # start = 0
        # result = 1

        # #alluniq = True
        # while start < len(s) - 1:
        #     seen = set()
        #     seen.add(s[start])
        #     next_item = start + 1
            
        #     while next_item < len(s):
        #         if s[next_item] not in seen:
        #             seen.add(s[next_item])
        #             next_item += 1
        #         else:
        #             #alluniq = False
        #             result = max(result, len(seen))
        #             break
        #     # if alluniq:
        #     #     break
        #     start += 1
            
        # # if alluniq:
        # #     return len(s)
        # return result


        start_index = 0
        end_index = 0
        seen = set() 
        result = 0
        while start_index < len(s) and end_index < len(s):
            if s[end_index] not in seen:
                seen.add(s[end_index])
                curr_length = ( end_index - start_index ) + 1
                result = max(result, curr_length)
                end_index += 1
            else:
                seen.remove(s[start_index])
                start_index += 1
        return result
        