from collections import defaultdict
from typing import List

"""

Course Schedule IV
https://leetcode.com/problems/course-schedule-iv/

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.


Algo
This is similar to find all the ancestors of each node in a DAG

1. Find all the ancestors of each node and store it as a list of ancestors for each node
2. iterate the Queries,
    ans = [False] * len(queries)
    for q in range(len(queries)):
            course1 = queries[q][0]
            course2 = queries[q][1]
            if course1 in listofancestors[course2]:
                ans[q] = True 

Khans Algorithm ( V + E ) + (#Q * V)
Final BigO should be (Q * V)


what is the time complexity coming? looks like O(V+E) + O( query * V) , in the last loop of Queries, the worst case is if b is the last node in a skewed tree where all the other nodes are the ancestors making it (Q * V) where Q is number of query,

O(V+E) + O( query * V)

so whats is actually O(V + E)
There can be (N-1)(N)/2 edges in a DAG, here N = 100 which makes it 4950
E = ( 100 - 1)100 / 2 = 4950 V = 100 , makes it 4950 + 100 = 5k

Max Query is 10k,
So ideally it should be O( query * V) since this is dominating
"""

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        ans = [False] * len(queries)

        # There are no prerequisites, and each course is independent.
        if not prerequisites:
            return ans

        self.g = defaultdict(list)

        indegree = [0] * numCourses

        for course1, course2 in prerequisites:
            self.g[course1].append(course2)
            indegree[course2] += 1

        ancestors = [ set() for _ in range(numCourses)]

        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.pop(0)

            for edge in self.g[course]:
                ancestors[edge].add(course)
                ancestors[edge].update(ancestors[course])
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    q.append(edge)

        listofancestors = [ list(ancestor) for ancestor in ancestors]

        for q in range(len(queries)):
            course1 = queries[q][0]
            course2 = queries[q][1]
            if course1 in listofancestors[course2]:
                ans[q] = True 
        return ans

numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]


numCourses = 2
prerequisites = []
queries = [[1,0],[0,1]]

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

s = Solution()
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))
