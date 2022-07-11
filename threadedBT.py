# Threaded binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        # true if the right child of the node points to its inorder successor
        self.isThreaded = 0


# Convert a BT to threaded Binary Tree using Queue
def findleft(root):
    node = root
    while node and node.left:
        node = node.left
    return node

def convert(root, q):
   if root:
       convert(root.left, q)
       q.pop(0)
       convert(root.right, q)
       if root.right is None and len(q) > 0:
           root.right = q[0]
           root.isThreaded = 1

def inorder_traversal(root):
    cur = findleft(root)
    while cur:
        print(cur.data)
        if cur.isThreaded == 1:
            cur = cur.right
        else:
            cur = findleft(cur.right)

def inorder_insertqueue(root, queue):
    if root:
        inorder_insertqueue(root.left, queue)
        queue.append(root)
        inorder_insertqueue(root.right, queue)
    return queue

def convertToThreaded(root):
    queue = []
    q = inorder_insertqueue(root, queue)    
    convert(root, q)


root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(3)
root.right.right.left = Node(8)
root.right.right.right = Node(10)

# convertToThreaded(root)
# print(root.data)
# inorder_traversal(root)

# Not using Queue a better Solution with O(1) space 

def convert(root):
    if not root:
        return 
    if not root.left and not root.right:
        return root
    if root.left:
        node = convert(root.left)
        node.right = root
        node.isThreaded = 1
    if not root.right:
        return root 
    return convert(root.right)
convert(root)
inorder_traversal(root)




