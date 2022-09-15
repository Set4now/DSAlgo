repository=["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery="mouse"

# def helper(search_str, repository):
#     max_result = 3
#     temp = []
#     for words in repository:
#         if words.lower().startswith(search_str.lower()):
#             temp.append(words)
#     temp.sort()
#     if len(temp) > max_result:
#         return temp[:max_result]
#     return temp


# def searchqueries(repository, customerQuery):
#     min_query_char = 2
#     pointer = min_query_char
#     search_str = ""
#     final_output = []
#     while pointer < len(customerQuery) + 1:
#         search_str = customerQuery[:pointer]
#         result = helper(search_str, repository)
#         if result:
#             final_output.append(result)
#         pointer += 1
#     return final_output



#print(searchqueries(repository, customerQuery))


from typing import List

class Solution:
    
    def helper(self, searchWord, products):
        print(products)
        max_result = 3
        temp = []
        for words in products:
            print ("checking searchstr {} in keyword {}: result: [{}]".format(
                searchWord,
                words,
                words.lower().startswith(searchWord.lower())
            ))
            if words.lower().startswith(searchWord.lower()):
                temp.append(words)
        temp.sort()
        if len(temp) > max_result:
            return temp[:max_result]
        return temp
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        min_query_char = 2
        pointer = min_query_char
        search_str = ""
        final_output = []
        while pointer < len(searchWord) + 1:
            search_str = searchWord[:pointer]
            # print(search_str)
            result = self.helper(search_str, products)
            if result:
                final_output.append(result)
            pointer += 1
        return final_output



a = Solution()
print(a.suggestedProducts(repository, customerQuery))