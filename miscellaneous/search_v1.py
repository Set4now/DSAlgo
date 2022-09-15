from typing import List

class Solution:
    
    def helper(self, searchWord, products):
        max_result = 3
        temp = []
        for words in products:
            if len(temp) < max_result:
                if words.lower().startswith(searchWord.lower()):
                    temp.append(words)
            else:
                break
        return temp
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        min_query_char = 1
        pointer = min_query_char
        search_str = ""
        final_output = []
        while pointer < len(searchWord) + 1:
            search_str = searchWord[:pointer]
            result = self.helper(search_str, products)
            final_output.append(result)
            pointer += 1
        return final_output

repository=["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery="mouse"

a = Solution()
print(a.suggestedProducts(repository, customerQuery))