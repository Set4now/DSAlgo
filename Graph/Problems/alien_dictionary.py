"""
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
Find the order of characters in the alien language.

Note: Many orders may be possible for a particular test case, 
thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Approach using topological sort

Observation, we need to return the order of alphabets the dictionary is following, by which it is currently sorted.
The other way to say is the words of dictionary is sorted based on a certain order of alphabets (like in english a,b,c,d...z)

The questions boils down to the fact of topological sorting, where the smallest alphabets will come first followed by biggest
means, eg, a will come first then b, b will come first than c.. and so in...

So we can create a DAG graph by comparing words to see which alphabet is smaller than which alphabet among K number of alphabets used in dictionary


Since the input dict of words is sorted,

1. Match each word with its next word  in the dict of words (input),
   if char is not matching then create 
    an edge like u --> v where u is from word1 and v is from word2
    (u,v) means pair of first not matched character from both words 
    and u is smaller than v, since the words are sorted (ascending order)

    create a graph (DAG) where u > [v1,v2...] means u has a directed edge to v1,v2... and
    also add the alphabets in self.nodes to track all the diff alphabets used in the words in dictionary

2.The edge case is, in the input there is K which denotes the number of alphabets used in the dictionary.
In setup 1, we will also maintain a set of all alphabets found, after performing step1, 
we might not get all the alphabets as mentioned in K used in the dictionary input

So we will iterate each char from each word from input dict,
and just add the unfound alphabets to set of alphabets found.

Now we have a list of all the alphabets (which is equal to K) and a graph (DAG) adjacency list representation


3. Now perform a topological sort on self.graph
   and return the topological order as result


"""

from collections import defaultdict

class Solution:
    def findOrder(self,aliendict, N, K):
        # code here
        self.nodes = set()
        self.g = defaultdict(list)
        i = 0
        while i < len(aliendict) - 1:
            word1 = aliendict[i]
            word2 = aliendict[i+1]
            
            wl1 = 0
            wl2 = 0
            # compare alphabet at index wl1 and wl2 from both words at a same time
            # stop whenever a char is not matched
            # since word1 comes before word2. means char from  word1 is smaller from char in word2
            # means char from  word1 will become u and char from word2 will become v
            # u :[v1,v2..]
            while wl1 < len(word1) and wl2 < len(word2):
                if word1[wl1] != word2[wl2]:
                    if word2[wl2] not in self.g[word1[wl1]]:
                        self.g[word1[wl1]].append(word2[wl2])
                    self.nodes.add(word1[wl1])
                    self.nodes.add(word2[wl2])
                    break
                else: #if matched, then go for next chars, keep doing until a mistmach found
                    wl1 += 1
                    wl2 += 1
                    
            i += 1
        
        # Covering an edge case mentioned in above explanation, to make sure we perform toplogical sorting on all alphabets (== k)
        for word in aliendict:
            for char in word:
                if char not in self.nodes:
                    self.nodes.add(char)
                    if len(self.nodes) == K:
                        break

        # return toplogical sort order
        return self.topologicalsort()

    
    def topologicalsort(self): 
        stack = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.dfs(node, visited, stack)
        return stack[::-1]
        
    
    def dfs(self, node, visited, stack):
        visited.add(node)
        for edge in self.g[node]:
            if edge not in visited:
                self.dfs(edge, visited, stack)
        stack.append(node)


s = Solution()

dict = ["baa","abcd","abca","cab","cad"]
n = 5
k = 4



dict = ['hhb', 'blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji', 'cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj', 'dlgdhiha', 'ehggedljjhfldcajeceaeehkalkfeidhigkifjl', 'gdalgkblahcldahledfghjb', 'geldbblaaflegjhlfjlgblfbdc', 'ibjceciedbiilkjliijgklcgliaeeic', 'jcebjkfgfibfckfiikklecihik', 'jdkcabjjjckgdblkljf', 'jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih', 'kfd', 'lhdgidialgabfklffahiihceflebfidl']

n = 13
k = 12
print(s.findOrder(dict, n, k))







# def show_smallest(word1, word2):
#     alphabets = dict(zip(string.ascii_lowercase, range(1,27)))

#     w1 = len(word1)
#     w2 = len(word2)

#     i = 0
#     j = 0
#     while i < w1 and j < w2:
#         if alphabets[word1[i]] < alphabets[word2[j]]:
#             return word1
#         elif alphabets[word1[i]] > alphabets[word2[j]]:
#             return word2
#         elif alphabets[word1[i]] == alphabets[word2[j]]:
#             i += 1
#             j += 1


# print(show_smallest("baaz", "bz"))

