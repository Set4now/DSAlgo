class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertNode(rootnode, nodevalue):
    '''Recursive approach
       Time / Space O(log N)
    '''
    if rootnode.data == None:
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:
        if not rootnode.leftchild:
            rootnode.leftchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        if not rootnode.rightchild:
            rootnode.rightchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.rightchild, nodevalue)
    # return "Nodes inserted successfully"

def preorder(rootnode):
    # O(N) root -> lefttree -> righttree
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

def inorder(rootnode):
    # O(N) lefttree -> root -> righttree
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

def postorder(rootnode):
    # O(N) lefttree -> righttree -> root
    if not rootnode:
        return
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)
    print(rootnode.data)
    
def levelorder(rootnode):
    # Using Queue, already discussed in BT tutorial
    # Time & Space O(N)
    pass

def searchnode(rootnode, nodevalue):
    # Time/ Space is O(log N)
    if nodevalue == rootnode.data:
        return True
    elif nodevalue < rootnode.data:
        if rootnode.leftchild:
            return searchnode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        if rootnode.rightchild:
            return searchnode(rootnode.rightchild, nodevalue)
    return False


def find_min(rootnode):
    cur = rootnode
    while cur.leftchild:
        cur = cur.leftchild
    return cur
    
            
# def deleteNode(root, key):
#         if not root:
#             return root
#         elif key < root.val:
#             root.left = deleteNode(root.left, key)
#         elif key > root.val:
#             root.right = deleteNode(root.right, key)
#         else:
#             #leaf
#             if not root.left and not root.right:
#                 root = None
#             # 1 child
#             elif not root.left:
#                 root = root.right
#             elif not root.right:
#                 root = root.left
#             # 2 children
#             else:
#                 temp = find_min(root.right)
#                 root.val = temp.val
#                 root.right = deleteNode(root.right, temp.val)
#         return root

def findlargest(root):
    node = root
    while node.rightchild:
        node = node.rightchild
    return node

def deleteNodeBST(root, key):
    if not root:
        return root
    elif root.data > key:
        root.leftchild =  deleteNodeBST(root.leftchild, key)
    elif root.data < key:
        root.rightchild =  deleteNodeBST(root.rightchild, key)
    else: # root data matches with key (node found) root.data == key
        #case 1 leaf node
        if not root.leftchild and not root.rightchild:
            root = None
        elif root.leftchild:
            root = root.leftchild
        elif root.rightchild:
            root = root.rightchild
        else:
            largest_node_lefttree = findlargest(root.leftchild)
            # replacing the target node value with largest node value
            root.data = largest_node_lefttree.data
            # now its time to delete the largest node 
            root.leftchild = deleteNodeBST(root.leftchild, largest_node_lefttree.data)
    return root
            
    


newbst = BSTNode(None)
insertNode(newbst, 40)
insertNode(newbst, 70)
insertNode(newbst, 30)
insertNode(newbst, 100)
insertNode(newbst, 80)
insertNode(newbst, 110)

# print(newbst.leftchild.data)
# print(newbst.rightchild.data)
# print(newbst.rightchild.rightchild.data)
# print(newbst.rightchild.rightchild.rightchild.data)

# print(searchnode(newbst, 110))
# print(searchnode(newbst, 120))

# print(newbst.data)
# print(searchnode(newbst, 40))

inorder(newbst)
print(deleteNodeBST(newbst, 80))
print(searchnode(newbst, 80))
inorder(newbst)
# print(find_min(newbst.rightchild))

# find LCA
def lca(root, a, b):
    if not root:
        return 
    if root.data >= a and root.data >= b:
        return lca(root.leftchild, a, b)
    if root.data <= a and root.data <= b:
        return lca(root.rightchild, a, b)
    if root.data >= a and root.data <= b:
        return root

def finddistance(root, key):
    if root.data == key:
        return 0
    if root.data >= key:
        return 1 + finddistance(root.leftchild, key)
    if root.data <= key:
        return 1 + finddistance(root.rightchild, key)

def findmindistance(root, keya, keyb):
    if not root:
        return 0
    if root.data >= keya and root.data >= keyb:
        return findmindistance(root.leftchild, keya, keyb)
    if root.data <= keya and root.data <= keyb:
        return findmindistance(root.rightchild, keya, keyb)
    if root.data >= keya and root.data <= keyb:
        return finddistance(root, keya) + finddistance(root, keyb)


# newbst = BSTNode(None)
# insertNode(newbst, 20)
# insertNode(newbst, 10)
# insertNode(newbst, 5)
# insertNode(newbst, 15)
# insertNode(newbst, 30)
# insertNode(newbst, 25)
# insertNode(newbst, 35)


# insertNode(newbst, 40)
# insertNode(newbst, 70)
# insertNode(newbst, 30)
# insertNode(newbst, 100)
# insertNode(newbst, 80)
# insertNode(newbst, 110)

# print(findmindistance(newbst, 5, 35))
# The min node is the leftmost node in the left subtree which does not have leftchild
def findmin(root):
    if root:
        node = root
        while node.leftchild:
            node = node.leftchild
        return node.data
    return None

# The max node is the rightmosr node in the right subtree which does not have any rightchild
def findmax(root):
    if root:
        node = root
        while node.rightchild:
            node = node.rightchild
        return node.data
    return None

def checkifBST(root):
    if not root:
        return
    if root.leftchild and root.rightchild:
        if root.data >= findmax(root.leftchild) and root.data <= findmin(root.rightchild):
            return True
    if checkifBST(root.leftchild) and checkifBST(root.rightchild):
        return True
    return False

# newbst = BSTNode(6)
# newbst.leftchild = BSTNode(2)
# newbst.rightchild = BSTNode(8)

# newbst.leftchild.leftchild = BSTNode(1)
# newbst.leftchild.rightchild = BSTNode(9)

# newbst = BSTNode(None)
# insertNode(newbst, 6)
# insertNode(newbst, 2)
# insertNode(newbst, 8)
# insertNode(newbst, 1)
# insertNode(newbst, 9)
# insertNode(newbst, 25)
# insertNode(newbst, 35)


# print(checkifBST(newbst))


class ConvertToDLL:
    def __init__(self, root) -> None:
        self.root = root
        self.head = None
        self.tail = None

    def _convert(self, node, tail):
        if not node:
            return tail
        tail = self._convert(node.leftchild, tail)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.leftchild = self.tail
            self.tail.rightchild = node
        self.tail = node 
        self._convert(node.rightchild, self.tail)

    def showLinkedlist(self):
        curr = self.head
        view = []
        while curr:
            view.append(curr.data)
            curr = curr.rightchild
        return view
    
    def convert(self):
        tail = None
        self._convert(self.root, tail)

    def run(self):
        self.convert()
        return self.showLinkedlist()

# btdll = ConvertToDLL(newbst)
# print(btdll.run())
        
        
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
    
    def add(self, data):
        newnode =  Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            cur_tail = self.tail 
            cur_tail.next = newnode
            self.tail = newnode

def getMiddle(head):
    slow = head
    fast = head
    # Iterate till fast's next is null (fast reaches end)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # return the slow's data, which would be the middle element.
    return slow

def convert(head, tail):
    if head.data == tail.data:
        return BSTNode(head.data)
    else:
        middle_node = getMiddle(head)
        print("middlenode: {}".format(middle_node.data))
        root = BSTNode(middle_node.data)
        #find the ll for left subtree
        # finding the head and tail of left LL (node before the middle root)
        left_cur_head = head
        left_cur_tail = head
        while left_cur_tail.next.data != root.data:
            left_cur_tail = left_cur_tail.next
        #making the tail next to None
        left_cur_tail.next = None 
        root.leftchild = convert(left_cur_head, left_cur_tail)

        #find the LL for right subtree
        # head for right LL is node next to root
        # print(middle_node.data)
        if middle_node.next:
            rt_head = middle_node.next
            rt_tail = rt_head
            print(rt_head, rt_tail)
            while rt_tail:
                if rt_tail.next:
                    rt_tail = rt_tail.next
                else:
                    break
            
            #making the tail next to None
            rt_tail.next = None
            root.rightchild = convert(rt_head, rt_tail)
        
        return root

def inorder(rootnode):
    # O(N) lefttree -> root -> righttree
    if not rootnode:
        return
    preorder(rootnode.leftchild)
    print(rootnode.data)
    preorder(rootnode.rightchild)


# ll = LinkedList()
# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.add(4)
# ll.add(5)
# ll.add(6)
# ll.add(7)

# ll.add(-10)
# ll.add(-3)
# ll.add(0)
# ll.add(5)
# ll.add(9)

# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.add(4)
# ll.add(5)

def convertLLtoBST(ll):
    # print(ll.head.data, ll.tail.data)
    root =  convert(ll.head, ll.tail)
    preorder(root)

# convertLLtoBST(ll)

    
# def coverttoBSTfromArr(arr):
#     pass 

arr = [-10,-3,0,5,9]
def convertarr(arr):
    if arr:
        if len(arr) == 1:
            return BSTNode(arr[0])
        else:
            # try:
            mid_index = len(arr) // 2
            # print(mid_index)
            # print(arr)
            root = BSTNode(arr[mid_index])
            # print(root.data)
            root.leftchild = convertarr(arr[:mid_index])
            
            root.rightchild = convertarr(arr[mid_index + 1:])
            # except Exception as e:
            #     print (str(e), mid_index)
            return root

# preorder(convertarr(arr))

def kthsmallest(root, k):
    current_count = 0
    return countnode(root, k, current_count)[0]

def countnode(root, k, current_count):
    if not root:
        return None, current_count
    left, current_count = countnode(root.leftchild, k, current_count)
    if left:
        return left, current_count
    current_count += 1
    if current_count == k:
        return root.data, current_count
    return countnode(root.rightchild, k, current_count)
    


    
newbst = BSTNode(None)
insertNode(newbst, 6)
insertNode(newbst, 2)
insertNode(newbst, 8)
insertNode(newbst, 1)
insertNode(newbst, 9)
insertNode(newbst, 25)
insertNode(newbst, 35)

# print(newbst.data)
# print(newbst.leftchild.data)
# print(newbst.rightchild.data)


def inorder(rootnode):
    # O(N) lefttree -> root -> righttree
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

# print(newbst.leftchild.leftchild.data)
# print (inorder(newbst))
# print(kthsmallest(newbst, 7))



def findfloorceil(root, key, floor, ceil):
    if not root:
        return floor, ceil
    if root.data > key:
        ceil = root
        floor, ceil = findfloorceil(root.leftchild, key, floor, ceil)
    if root.data < key:
        floor = root
        floor, ceil = findfloorceil(root.rightchild, key, floor, ceil)
    if root.data == key:
        floor = ceil = root
        return floor, ceil
    return floor, ceil

newbst = BSTNode(None)
insertNode(newbst, 8)
insertNode(newbst, 6)
insertNode(newbst, 15)
insertNode(newbst, 2)
insertNode(newbst, 7)
insertNode(newbst, 15)
insertNode(newbst, 20)
insertNode(newbst, 5)

def showceilfloor(key):
    floor, ceil = findfloorceil(newbst, key, None, None)
    if floor and ceil:
        print(floor.data, ceil.data)
    else:
        if not floor:
             print(floor, ceil.data)
        if not ceil:
             print(floor.data, ceil)

# showceilfloor(1)

