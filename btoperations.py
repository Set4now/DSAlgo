class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

import copy

# def printallpaths(rootnode, path, res):
#     # if res is not None and path is not None:
#     path.append(rootnode.data)
#     if rootnode.leftchild or rootnode.rightchild:
#         if rootnode.leftchild:
#             printallpaths(rootnode.leftchild, path, res)
#         if rootnode.rightchild:
#             printallpaths(rootnode.rightchild, path, res)
#     else:
#         # res.append(copy.deepcopy(path))
#         print(path)
#         # print (res)
#     path.pop()

def depthofnode(rootnode, keynodevalue, depth=0):
    if not rootnode:
        return 0
    if rootnode.data == keynodevalue:
        return depth
    left_depth = depthofnode(rootnode.leftchild, keynodevalue, depth+1)
    right_depth = depthofnode(rootnode.rightchild, keynodevalue, depth+1)
    return max(left_depth, right_depth)

A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")

A.leftchild = B
A.rightchild = C 

B.leftchild = D
B.rightchild = E 

F = TreeNode("F")
E.leftchild = F

G = TreeNode("G")
H = TreeNode("H")

C.leftchild = G
C.rightchild = H

#  ============= 2nd BT 
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.leftchild = b
a.rightchild = c

b.leftchild = d
b.rightchild = e 

f = TreeNode("F")
e.leftchild = f

g = TreeNode("G")
h = TreeNode("H")

c.leftchild = g
c.rightchild = h

# i = TreeNode("I")
# h.leftchild = i

# print(depthofnode(A, "F"))

# def getpath():
#     path = []
#     res = []
#     printallpaths(A, path, res)
#     print(res)
#     # return result

# Print all paths from the root to leaf nodes of a binary tree
def showallpaths(rootnode, path=None):
   if not rootnode:
      return 
   path.append(rootnode.data)
   if not rootnode.leftchild and not rootnode.rightchild:
      print ("->".join(path))
   else:
      showallpaths(rootnode.leftchild, path)
      showallpaths(rootnode.rightchild, path)
   path.pop()
   
# showallpaths(A, path=[])

# print(getpath())
# print (printallpaths(A, path=[]))

def _longestpath(rootnode, path, longestpath):
   if not rootnode:
      return 
   path.append(rootnode.data)
   if not rootnode.leftchild and not rootnode.rightchild:
      if len(path) >= len(longestpath):
         longestpath.append(copy.deepcopy(path))
   else:
       _longestpath(rootnode.leftchild, path, longestpath)
       _longestpath(rootnode.rightchild, path, longestpath)
   path.pop()

def printpath(rootnode):
    longestpath = []
    _longestpath(rootnode, [], longestpath)
    longest = []
    for path in longestpath:
        if len(path) > len(longest):
            longest = path
    print (longest)
# \

###### Find distance between given pairs of nodes in a binary tree #####
def getnodepath(rootnode, key, path):
    if not rootnode:
        return 
    path.append(rootnode.data)
    if rootnode.data == key:
        return True
    
    dataatleft = getnodepath(rootnode.leftchild, key, path)
    dataatright = getnodepath(rootnode.rightchild, key, path)

    if dataatleft or dataatright:
        return True
    else:
        path.pop()
        return False

def nodesdistance():
    # path for node a
    pathone = []
    getnodepath(A, "F", pathone)

    # path for node a
    pathtwo = []
    getnodepath(A, "C", pathtwo)

    # LCA (least common ancestor)
    # from LCA , ( path/edges of node a + node b )
    distinct = []
    for item in pathone:
        if item not in pathtwo:
            distinct.append(item)
    
    for item in pathtwo:
        if item not in pathone:
            distinct.append(item)
    print(len(distinct))

# nodesdistance()

def searchnode(rootnode, key):
    if not rootnode:
        return
    if rootnode.data == key:
        return True
    leftdata = searchnode(rootnode.leftchild, key)
    rightdata = searchnode(rootnode.rightchild, key)
    if leftdata or rightdata:
        return True
    return False

def aretreeidentical(rootnodea, rootnodeb):
    # (Base case)
    # if both trees are empty, return true , for leaf nodes as well
    if not rootnodea and not rootnodeb:
        return True
    if not rootnodea or not rootnodeb:
        return False
    if rootnodea.data != rootnodeb.data:
        return False
    
    leftnode = aretreeidentical(rootnodea.leftchild, rootnodeb.leftchild)
    rightnode = aretreeidentical(rootnodea.rightchild, rootnodeb.rightchild)
    # False if any mismatch in either left or right subtree
    if not leftnode or not rightnode:
        return False
    return True

    # print(searchnode(A, "X"))
# print(aretreeidentical(A, a))





def _topview(rootnode, dist, level, map):
    if not rootnode:
        return
    if dist not in map.keys():
        map[dist] = (rootnode.data, level)
    else:
        existing_node, existing_level = map[dist]
        if level < existing_level:
            map[dist] = (rootnode.data, level)
    _topview(rootnode.leftchild, dist - 1, level + 1 , map)
    _topview(rootnode.rightchild, dist + 1, level + 1, map)

def _bottomview(rootnode, dist, level, map):
    if not rootnode:
        return
    if dist not in map.keys():
        map[dist] = (rootnode.data, level)
    else:
        existing_node, existing_level = map[dist]
        if level >= existing_level:
            map[dist] = (rootnode.data, level)
    _bottomview(rootnode.leftchild, dist - 1, level + 1 , map)
    _bottomview(rootnode.rightchild, dist + 1, level + 1, map)


def printtopview():
    distmap = {}
    rootdist = 0
    rootlevel = 0 
    # _topview(A, rootdist, rootlevel, distmap)
    # OR
    _bottomview(A, rootdist, rootlevel, distmap)
    #print(distmap)
    # {0: ('A', 0), -1: ('B', 1), -2: ('D', 2), 1: ('C', 1), 2: ('H', 2)}
    sorteddist = sorted(distmap.items())
    # print(sorteddist)
    #[(-2, ('D', 2)), (-1, ('B', 1)), (0, ('A', 0)), (1, ('C', 1)), (2, ('H', 2))]
    final_result = []
    for nodedata in sorteddist:
        final_result.append(nodedata[1][0])
    print(final_result)
# printtopview()
# ['D', 'B', 'A', 'C', 'H'] -> top view
# ['D', 'F', 'G', 'C', 'H'] -> bottom view
def preOrder(rootnode):
   if not rootnode:
      return 
   stack = []
   stack.append(rootnode)
   while stack:
      poppednode = stack.pop()
      print (poppednode.data)
      if poppednode.rightchild:
         stack.append(poppednode.rightchild)
      if poppednode.leftchild:
         stack.append(poppednode.leftchild)
# preOrder(A)
def inorder(rootnode):
    if not rootnode:
        return False 
    curr_node = rootnode
    stack = []
    while stack or curr_node:
        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.leftchild
        else:
            poppednode = stack.pop()
            print(poppednode.data)
            curr_node = poppednode.rightchild
            

# inorder(A)
#In-place convert a binary tree to its sum tree
def sumtree(rootnode):
    if not rootnode:
        return 0
    new_sum = sumtree(rootnode.leftchild) + sumtree(rootnode.rightchild)
    old_data = rootnode.data
    rootnode.data = new_sum
    return old_data + new_sum

A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")

A.leftchild = B
A.rightchild = C

B.leftchild = D
B.rightchild = E

F = TreeNode("F")
C.leftchild = F
G = TreeNode("G")
C.rightchild = G
# preOrder(A)
# sumtree(A)
# preOrder(A)

# Determine whether the given binary tree nodes are cousins of each other
'''
Given a binary tree, determine if two given nodes are cousins of each other or not.
Two nodes of a binary tree are cousins of each other only if they have different parents, 
but they are at the same level.
For example, consider the following tree:

Level Order Traversal










(4, 6), (4, 7), (5, 6) and (5, 7) are cousins of each other.
(2, 3), (4, 5), (6, 7), (4, 3), etc., are not cousins of each other.

Algorithm
Traverse the tree and store a map of each node as key and value as  their level and parent node. 
{node: (parent, level)}
If both nodes are present at the same level and have different parents, they are cousins. 
If their level is different, or they are a sibling, they cannot be cousins.
'''
def createlevelparentmap(parent, node, level, mapper):
    mapper[node] = (parent, level)

def preOrder(parentnode, rootnode, level, mapper):
    #Keeping a map of nodes to its parent and current level
    if not rootnode:
        return 
    if rootnode not in mapper.keys():
        createlevelparentmap(parentnode, rootnode, level, mapper)
    preOrder(rootnode, rootnode.leftchild, level + 1, mapper)
    preOrder(rootnode, rootnode.rightchild, level + 1, mapper)

    
def checkcousins(rootnode, nodea, nodeb):
    mapper = {}
    # map for storing each node as key and value as  their level and parent node
    mapper[rootnode] = None
    rootlevel = 1
    # perform preorder  on left subtree
    preOrder(rootnode, rootnode.leftchild, rootlevel + 1, mapper)
    # perform preorder  on right subtree
    preOrder(rootnode, rootnode.rightchild, rootlevel + 1, mapper)
    # check if both nodes have diff parent and same level
    if not (mapper[nodea][0] is mapper[nodeb][0]) and (mapper[nodea][1] == mapper[nodeb][1]):
       print (True)
    else:
       print(False)

# checkcousins(A, F, G)


def _checkifsumtree(rootnode):
   if not rootnode:
        return 0
   if not rootnode.leftchild and not rootnode.rightchild:
      return rootnode.data
   total = _checkifsumtree(rootnode.leftchild) + _checkifsumtree(rootnode.rightchild)
   if rootnode.data == total:
       return rootnode.data + total
   else:
       return False
def sumtreechecker(rootnode):
    if not rootnode:
        return 0
    if not rootnode.leftchild and not rootnode.rightchild:
      return rootnode.data
    result = _checkifsumtree(rootnode)
    print(result)
    if rootnode.data == result / 2:
        return True
    return False
    




A = TreeNode(44)
B = TreeNode(9)
C = TreeNode(13)
D = TreeNode(5)
E = TreeNode(4)
F = TreeNode(6)
G = TreeNode(7)

A.leftchild = B
A.rightchild = C

B.leftchild = D
B.rightchild = E

C.leftchild = F
C.rightchild = G

# another example
A = TreeNode(56)
B = TreeNode(13)
C = TreeNode(15)
A.leftchild = B
A.rightchild = C


D = TreeNode(5)
E = TreeNode(3)
B.leftchild = D
B.rightchild = E

F = TreeNode(9)
G = TreeNode(3)
C.leftchild = F
C.rightchild = G

H = TreeNode(3)
I= TreeNode(2)

D.leftchild = H
D.rightchild = I

J = TreeNode(2)
K = TreeNode(1)

G.leftchild = J
G.rightchild = K


# print(sumtreechecker(A))

#Determine whether a binary tree is a subtree of another binary tree
def checkfornode(rootnode, keynode):
    if not rootnode:
       return 
    if rootnode.data == keynode.data:
       return (rootnode, keynode)
    #    return True
    leftcheck = checkfornode(rootnode.leftchild, keynode)
    rightcheck = checkfornode(rootnode.rightchild, keynode)
    if leftcheck or rightcheck:
        # if true then return both the nodes
        if leftcheck:
            return leftcheck
        return rightcheck
    return False

def treevalidator(rootnodea, rootnodeb):
    if not rootnodea and not rootnodeb:
      return True
    # if not rootnodea or not rootnodeb:
    #   return False
    if rootnodea.data != rootnodeb.data:
        return False
    leftcheck=treevalidator(rootnodea.leftchild, rootnodeb.leftchild)
    rightcheck=treevalidator(rootnodea.rightchild, rootnodeb.rightchild)
    if not leftcheck or not rightcheck:
        return False
    return True


def subtreecheck(rootnodea, rootnodeb):
    if rootnodea.data == rootnodeb.data:
        if not rootnodeb.leftchild and not rootnodeb.rightchild:
            return True
    returned_node_tuples = checkfornode(rootnodea, rootnodeb)
    if returned_node_tuples:
        rootnodeA, rootnodeB = returned_node_tuples
        # print(rootnodeA.data, rootnodeB.data)
        return  treevalidator(rootnodeA, rootnodeB)
    return False
##########
# A = TreeNode("3")
# B = TreeNode("4")
# C = TreeNode("5")
# D = TreeNode("1")
# E = TreeNode("2")

# A.leftchild = B
# A.rightchild = C 

# B.leftchild = D
# B.rightchild = E 

# F = TreeNode("0")
# # E.leftchild = F

# a = TreeNode("4")
# b = TreeNode("1")
# c = TreeNode("2")

# a.leftchild = b 
# a.rightchild = c

##########
A = TreeNode("1")
B = TreeNode("1")
A.leftchild = B

C = TreeNode("1")
D = TreeNode("1")
C.leftchild = D


# print(subtreecheck(A, C))

a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)

d = TreeNode(1)
e = TreeNode(2)
f = TreeNode(0)

a.leftchild = b
a.rightchild = c

b.leftchild = d
b.rightchild = e

e.leftchild = f

g = TreeNode(6)
c.rightchild = g

a1 = TreeNode(5)
# a2 = TreeNode(1)
# a3 = TreeNode(2)
# a1.leftchild = a2
# a1.rightchild = a3

nodelist = []
def __preorder(rootnode, nodelist, side=None):
    if not rootnode:
        nodelist.append(side)
        return 
    __preorder(rootnode.leftchild, nodelist, side="leftnull")
    nodelist.append(rootnode.data)
    __preorder(rootnode.rightchild, nodelist, side="rightnull")


# __preorder(a, nodelist)
# print(nodelist)

# nodelistb = []
# __preorder(a1, nodelistb)
# print(nodelistb)

def preOrder_ancestor(root, key, nodelist):
    if not root:
      return
    nodelist.append(root.data)
    if root.data == key.data:
       nodelist.pop()
    #    print(nodelist)
       return True
    leftcheck = preOrder_ancestor(root.leftchild, key, nodelist)
    rightcheck = preOrder_ancestor(root.rightchild, key, nodelist)
    if leftcheck or rightcheck:
        return True
    nodelist.pop()
    return False
def findancestores(root, keynode):
    nodelist  = []
    result = preOrder_ancestor(root, keynode, nodelist)
    print(result)
    print (nodelist)

a = TreeNode("1")


b = TreeNode("2")
c = TreeNode("3")

a.leftchild = b
a.rightchild = c

d = TreeNode("4")
e = TreeNode("5")

b.leftchild = d
b.rightchild = e

f = TreeNode("6")
g = TreeNode("7")

c.leftchild = f
c.rightchild = g

h = TreeNode("8")

f.leftchild = h

i = TreeNode("9")
g.rightchild = i

# findancestores(a, h)





def sumdiagonal(parentdiagonal, node, map, side):
    if not node:
       return
    if side == "left":
       nodediagonal = parentdiagonal - 1
    else:
       nodediagonal = parentdiagonal
    if nodediagonal not in map:
       map[nodediagonal] = node.data
    else:
       map[nodediagonal] += node.data
    sumdiagonal(nodediagonal, node.left, map, "left")
    sumdiagonal(nodediagonal, node.right, map, "right")

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(9)
root.left.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.right = TreeNode(7)
root.right.left.left = TreeNode(12)
root.left.right.left = TreeNode(11)
root.left.left.right = TreeNode(10)

def helper(root):
    if not root.left and root.rightL:
        return 0
    else:
        rootdiagonal = 0
        mapper = {rootdiagonal: root.data}
        sumdiagonal(rootdiagonal, root.left, mapper, "left")
        sumdiagonal(rootdiagonal, root.right, mapper, "right")
        print (list(mapper.values()))
# helper(root)


def fulltree(root):
    if not root:
        return
    # recursively truncate the left subtree and subtree first
    root.left = fulltree(root.left)
    root.right = fulltree(root.right)

    # do nothing if the current node is a leaf node or has two children
    if (not root.left and not root.right) or (root.left and root.right):
        return root

    # if the current node has exactly one child, delete it and replace
    # it with the child node
    if root.left:
        childnode = root.left
    else:
        childnode = root.right
    return childnode


def preorder(rootnode):
    if not rootnode:
        return 
    print(rootnode.data)
    preorder(rootnode.left)
    preorder(rootnode.right)

A = TreeNode(0)

B = TreeNode(1)
C = TreeNode(2)

A.left = B
A.right = C

D = TreeNode(3)
E = TreeNode(4)

B.left = D
C.left = E

F = TreeNode(5)
G = TreeNode(6)
H = TreeNode(7)

D.left = F
E.left = G
E.right = H

# preorder(A)
# print ("------------")
# print(fulltree(A))
# print ("------------")
# preorder(A)
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.right.left = TreeNode(4)
root.right.right = TreeNode(2)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(3)

def showcompletepaths(root, path=None):
    if not root:
        return
    path.append(root.data)
    if not root.left and root.right:
        print("-->".join(path))
        # finallist.append(copy.deepcopy(path))
    else:
        showcompletepaths(root.left, path)
        showcompletepaths(root.right, path)
    path.pop()

# allpaths = []
# showcompletepaths(root, [])
# print(allpaths)


def _showallpaths(rootnode, finallist, path=None):
   if not rootnode:
      return 
   path.append(rootnode.data)
   if not rootnode.left and not rootnode.right:
      finallist.append(copy.deepcopy(path))
   else:
      _showallpaths(rootnode.left, finallist, path)
      _showallpaths(rootnode.right, finallist, path)
   path.pop()
finallist = []
_showallpaths(root, finallist, [])
print(finallist)