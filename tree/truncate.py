import copy

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def truncate(root, sumk, target=0):
    if not root:
        return
    target += root.data
    if not root.left and not root.right:
        if target < sumk:
            return None
        return root
    else:
        root.left = truncate(root.left, sumk, target)
        root.right = truncate(root.right, sumk, target)
    if root.left or root.right:
        return root

k = 45
# root = Node(6)
# root.left = Node(3)
# root.right = Node(8)
# root.right.left = Node(4)
# root.right.right = Node(2)
# root.right.left.left = Node(1)
# root.right.left.right = Node(7)
# root.right.right.right = Node(3)
# root.right.right.right.right = Node(50)


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.left.left = Node(8)
# root.left.left.right = Node(9)
# root.left.right.left = Node(12)
# root.right.right.left = Node(10)
# root.right.right.left.right = Node(11)
# root.left.left.right.left = Node(13)
# root.left.left.right.right = Node(14)
# root.left.left.right.right.left = Node(15)

# truncate(root, k)
# inorder(root)

def maxsumpath(root, path, listofpaths):
    if not root:
        return
    path.append(root.data)
    if not root.left and not root.right:
        listofpaths.append(copy.deepcopy(path))
    else:
        maxsumpath(root.left, path, listofpaths)
        maxsumpath(root.right, path, listofpaths)
    path.pop()

listofpaths  = []

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(8)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.right.left = Node(10)
root.right.left.left = Node(7)
root.right.left.right = Node(9)
root.right.right.right = Node(5)

def printmaxsumpath(listofpaths):
    maxsum = 0
    cur_path = []
    for path in listofpaths:
        if sum(path) > maxsum:
            maxsum = sum(path)
            cur_path = path
    print("max sum is : {}".format(maxsum))
    print("path for max sum is : {}".format(cur_path))

maxsumpath(root, [], listofpaths)
printmaxsumpath(listofpaths)

# max sum is : 18
# path for max sum is : [1, 3, 5, 9]