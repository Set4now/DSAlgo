class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printpaths(root):
    if not root:
        return []
    results = []
    stack = [(root, str(root.data))]
    while stack:
        curr, curr_path = stack.pop()
        if not curr.left and not curr.right:
            results.append((curr_path))
        if curr.right:
            stack.append((curr.right, curr_path+"->"+str(curr.right.data)))
        if curr.left:
            stack.append((curr.left, curr_path+"->"+str(curr.left.data)))
    return results 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)
# print(printpaths(root))

import copy
def getallleadfpaths(root, dist, path, allpaths):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        allpaths.append(copy.deepcopy(path))
    else:
        getallleadfpaths(root.left, dist, path, allpaths)
        getallleadfpaths(root.right, dist, path, allpaths)
    path.pop()

def nodesatKdistancefromleaf(root, dist):
    allpaths = []
    getallleadfpaths(root, dist, [], allpaths)
    resultnodes = set()
    for path in allpaths:
        path.reverse() # to get the direction from leaf to root
        if dist < len(path):
            resultnodes.add(path[dist])
    return list(resultnodes)

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
root.right.left.left = Node(18)

dist = 3
# print(nodesatKdistancefromleaf(root, dist))


def treecount(root, count):
    if not root:
        return 0, count
    if not root.left and not root.right:
        count += 1
        return root, count
    else:
        leftnode, count = treecount(root.left, count)
        rightnode, count = treecount(root.right, count)
    if leftnode and rightnode:
        if root.data == leftnode.data and root.data == rightnode.data:
            count += 1
    else:
        if leftnode:
            if root.data == leftnode.data:
                count += 1
        if rightnode:
            if root.data == rightnode.data:
                count += 1
    return root, count


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(4)
root.right.left.left = Node(5)
root.right.left.right = Node(5)
root.right.right.right = Node(7)
# print(treecount(root, 0)[1])


def findmaxdiff(root, path, maxdiff):
    if not root:
        return maxdiff
    path.append(root.data)
    if not root.left and not root.right:
        curr_diff = max(path) - min(path)
        if curr_diff > maxdiff:
            maxdiff = curr_diff
    maxdiff = findmaxdiff(root.left, path, maxdiff)
    maxdiff = findmaxdiff(root.right, path, maxdiff)
    path.pop()
    return maxdiff

root = Node(6)
root.left = Node(3)
root.right = Node(8)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(7)

print(findmaxdiff(root, [], 0))
