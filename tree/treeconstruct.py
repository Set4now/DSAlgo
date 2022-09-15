class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.data, end=' ')
    inorderTraversal(root.right)

def construct(inorder, d):
    if not inorder:
        return None
    # find the node in inorder which has min level order index
    if len(inorder) > 1:
        toberootnodeval = len(inorder)
        for nodeval in inorder:
            if d[nodeval] < toberootnodeval:
                toberootnodeval = nodeval
    else:
        toberootnodeval = inorder[0]
    root = Node(toberootnodeval)
    mid = inorder.index(root.data)
    root.left = construct(inorder[:mid], d)
    root.right = construct(inorder[mid+1:], d)
    return root


def helper():
    inorder = [4, 2, 5, 1, 6, 3, 7]
    level = [1, 2, 3, 4, 5, 6, 7]
    d = {}
    for i,j in enumerate(level):
        d[j] = i 
    # print(d)
    root = construct(inorder, d)
    print('Inorder traversal of the constructed tree is ', end='')
    inorderTraversal(root)

# helper()
def construct(start, preorder, boolarray):
    if start < len(preorder):
        if boolarray[start] == 1:
            node = Node(preorder[start])
            start += 1
            return node, start
        else:
            root = Node(preorder[start])
            start += 1
            root.left, start = construct(start, preorder, boolarray)
            root.right, start = construct(start, preorder, boolarray)
        return root, start


def preorderTraversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)

# preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]
# isLeaf = [0, 0, 1, 1, 0, 0, 1, 1, 1]
# root = construct(0, preorder, isLeaf)[0]

# print the tree in a preorder fashion
# print('Preorder traversal of the constructed tree is', end=' ')
# preorderTraversal(root)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

def getlevels(root, level, mapper):
    if not root:
        return None, level, mapper 
    if level % 2 == 0:
        mapper["even"] += root.data
    else:
        mapper["odd"] += root.data
    getlevels(root.left, level + 1, mapper)
    getlevels(root.right, level + 1, mapper)

# d = {"odd": 0, "even": 0}
# getlevels(root, 0, d)
# print(d["even"] - d["odd"])

#########################
class Node:
    # Constructor
    def __init__(self, data, left=None, right=None, random=None):
        self.data = data
        self.left = left
        self.right = right
        self.random = random

def create_map_randompointer(root, orig_t):
    if not root:
        return
    cloned_node = Node(root.data)
    orig_t[root] = cloned_node
    cloned_node.left = create_map_randompointer(root.left, orig_t)
    cloned_node.right = create_map_randompointer(root.right, orig_t)
    return cloned_node

def get_cloned_root(root):
    orig_t = {}
    cloned_root = create_map_randompointer(root, orig_t)
    for orig_node, cloned_node in orig_t.items():
        cloned_node.random = orig_node.random
    return cloned_root

# Function to print the preorder traversal on a given binary tree
def preorder(root):
    if root is None:
        return
    # print the current node's data
    print(root.data, end=' —> (')
    # print left child's data
    print((root.left.data if root.left else 'X'), end=', ')
    # print the right child's data
    print((root.right.data if root.right else 'X'), end=', ')
    # print the random child's data
    print(str(root.random.data if root.random else 'X') + ')')
    # recur for the left and right subtree
    preorder(root.left)
    preorder(root.right)
    
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    root.left.left.random = root.right
    root.left.right.random = root
    root.right.left.random = root.left.left
    root.random = root.left
 
    print('Preorder traversal of the original tree:')
    preorder(root)
 
    clone_root = get_cloned_root(root)
 
    print('\nPreorder traversal of the cloned tree:')
    preorder(clone_root)