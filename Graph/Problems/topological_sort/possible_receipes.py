from collections import defaultdict
from typing import List

"""
 Find All Possible Recipes from Given Supplies
 https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

 You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Algorithm:
Topological Sort 

we will form a graph, ingredients ---> receipes (directed)
then perform Topological Sort using khan's algorithm

We will put all our initial supplies to the Supply Queue
then start popping each item from Supply Queue
For every popped item, check its edges (Recipies), if indegree becomes 0 , that means theat recipe can be made
So we add that recipe to the Supply Queue and ans array as well, since this recipe can be used as an ingredient to some recipe


TIme complexity (V + E)


"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.g = defaultdict(list)
        indegrees = {v: 0 for v in recipes}
        
        for i in range(len(recipes)):
            for j in ingredients[i]:
                self.g[j].append(recipes[i])
                indegrees[recipes[i]] += 1
                    
        q = []          
        for supply in supplies:
            q.append(supply)
        ans = []

        print(self.g)
                
        while q:
            item = q.pop(0)
            for edge in self.g[item]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                    ans.append(edge)
                    q.append(edge)
        return ans

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]


s = Solution()
print(s.findAllRecipes(recipes, ingredients, supplies))