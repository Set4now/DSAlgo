from collections import defaultdict
from typing import List

"""

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


Solution:
DSU problem

Algorithm
1. Process the "==" equations and join them using union (DSU)
2. Now Process the "!=" equations
   for any equation 
   s1 != s2
   if s1 and s2 belongs to a same set (from step 1),
   than return False 

   Because, from step 1, we did union all the similar variables
   Now this "!=" making those equations false

   eg,
   a==b, b==c, c==a , b!=c
   when we process all the "==" equations

   we got a set as {a.b,c} meaning a == b,b==a,a == c etc..all variables are eq to each other 
   This is the condition for the equations to be True

   Now in step 2 when we process !=
   we get b!=c
   b & c are in the same set {a.b,c} from step 1
   so, b!=c is not satisfying the condition

"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {}

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            if x not in parents:
                parents[x] = x
            if y not in parents:
                parents[y] = y

            p1 = find(x)
            p2 = find(y)

            if p1 != p2:
                parents[p2] = parents[p1]
                return True
            else:
                return False 
        
        def checksameset(x, y):
            if x not in parents:
                parents[x] = x
            if y not in parents:
                parents[y] = y

            p1 = find(x)
            p2 = find(y)

            if p1 == p2:
                return True
            return False


        for eq in equations:
            b = [i for i in eq] # ['a', '=', '=', 'b']
            var1 = b[0]
            var2 = b[3]
            if b[1] == "=":
                union(var1, var2)

        for eq in equations:
            b = [i for i in eq] # ['a', '=', '=', 'b']
            var1 = b[0]
            var2 = b[3]
            if b[1] == "!":
                # if any equation is false or does not satisfy the condition then the final ans will be False
                # since the question is asking to satisfy all the given equations
                if checksameset(var1, var2):
                    return False
        return True

equations = ["a==b","b!=a"]

equations = ["b==a","a==b"]

equations = ["a==b","b==c","a==c"]

equations = ["a==b","b!=c","c==a"]

equations = ["a!=b","b!=c","c!=a"]
s = Solution()
print(s.equationsPossible(equations))