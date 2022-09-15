# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import copy
# class Solution:
#     def sumNumbers(self, root) -> int:
#         allpaths = []
#         self.getpaths(root, [], allpaths)
#         finalsum = 0
#         print(allpaths)
#         for path in allpaths:
#             finalsum += sum(path)
#         return finalsum
    
def getpaths(root, path, allpaths):
    if not root:
        return
    path.append(root.val)
    if not root.left and not root.right:
        allpaths.append(copy.deepcopy(path))
    else:
        getpaths(root.left, path, allpaths)
        getpaths(root.right, path, allpaths)
    path.pop()

def sumNumbers(root):
    allpaths = []
    getpaths(root, [], allpaths)
    finalsum = 0
    # print(allpaths)
    for path in allpaths:
        finalsum += int("".join([str(i) for i in path]))
    return finalsum

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
A.left = B
A.right = C
print(sumNumbers(A))

