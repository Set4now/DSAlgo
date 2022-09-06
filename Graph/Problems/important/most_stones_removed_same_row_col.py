"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.


This is a DisjoinSet union find problem 

The idea is to find the number of connected components in a Graph

Then,

answer will be 
len(stones) - (# of components)

How will you find # of components and imagine the input as Graph

We need to group stones belonging to the either same row or same col
(union them)

Then find the number of unique parents, which will tell you 
the number of components in the graph


"""


from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parents = {}
        
        def find(x):
            if x != parents[x]:
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
                parents[p2] = p1
                
        for i,j in stones:
            print(i, ~j)
            union(i, ~j)
            print(parents)
        
        # The number of connected components can be number of roots ( parent of each component) , so if there are 2 components, means 2 parents
        # So we need to find the unique parents
        roots = set()
        for key in parents:
            roots.add(find(key))
        
        
        return len(stones) - len(roots)


s =Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

print(s.removeStones(stones))