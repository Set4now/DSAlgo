class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None
def postorder(rootnode):
    if not rootnode:
        return
    else:
        postorder(rootnode.leftchild)
        postorder(rootnode.rightchild)
        print (rootnode.data)
N1 = TreeNode("N1")
N2 = TreeNode("N2")
N3 = TreeNode("N3")
N4 = TreeNode("N4")
N5 = TreeNode("N5")
N1.leftchild = N2
N1.rightchild = N3
N2.leftchild = N4
N2.rightchild = N5
N6 = TreeNode("N6")
N7 = TreeNode("N7")
N3.leftchild = N6
N3.rightchild = N7
N9 = TreeNode("N9")
N10 = TreeNode("N10")
N4.leftchild = N9
N4.rightchild = N10
# postorder(N1)
'''
N9
N10
N4
N5
N2
N6
N7
N3
N1
'''
class Node:
    def __init__(self, val) -> None:
        self.val= val 
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
class Queue:
    def __init__(self) -> None:
        self.ll = LinkedList()
    def enqueue(self, bt_node):
        new_node = Node(bt_node)
        if self.ll.head is None:
            self.ll.head = new_node
            self.ll.tail = new_node
        else:
            cur_tail = self.ll.tail
            self.ll.tail = new_node
            cur_tail.next = new_node
    def dequeue(self):
        current_head = self.ll.head
        next_tobe_head = current_head.next
        self.ll.head = next_tobe_head
        return current_head
    def isEmpty(self):
        return True if self.ll.head is None else False
def levelorder(rootnode):
    if not rootnode:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(rootnode)
        while not custom_queue.isEmpty():
            dequeue_node = custom_queue.dequeue()
            print (dequeue_node.val.data)
            if dequeue_node.val.leftchild is not None:
                custom_queue.enqueue(dequeue_node.val.leftchild)
            if dequeue_node.val.rightchild is not None:
                custom_queue.enqueue(dequeue_node.val.rightchild)
# levelorder(N1)
'''
N1
N2
N3
N4
N5
N6
N7
N9
N10
'''

def searchnode(rootnode, nodevalue):
    if not rootnode:
        return "Binary Tree is empty"
    else:
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            poppednode = customqueue.dequeue()
            if poppednode.val.data == nodevalue:
                return True
            if poppednode.val.leftchild:
                customqueue.enqueue(poppednode.val.leftchild)
            if poppednode.val.rightchild:
                customqueue.enqueue(poppednode.val.rightchild)
        return False

#print(searchnode(N1, "N20"))

def insertnode(nodetoinsert, rootnode=None):
    if not rootnode:
        rootnode = nodetoinsert
        return 'Node insertion: Success'
    else:
        result = {"parentNode": "", "position": ""}
        customQueue = Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            poppednode = customQueue.dequeue()
            if not poppednode.val.leftchild:
                poppednode.val.leftchild = nodetoinsert
                result["parentNode"] = poppednode.val.data
                result["position"] = "Left"
                break
            else:
                customQueue.enqueue(poppednode.val.leftchild)
            if not poppednode.val.rightchild:
                poppednode.val.rightchild = nodetoinsert
                result["parentNode"] = poppednode.val.data
                result["position"] = "Right"
                break
            else:
                customQueue.enqueue(poppednode.val.rightchild)
        return "Insertion Success: {}".format(result)

N1 = TreeNode("N1")
N2 = TreeNode("N2")
N3 = TreeNode("N3")
N4 = TreeNode("N4")
N5 = TreeNode("N5")
N1.leftchild = N2
N1.rightchild = N3
N2.leftchild = N4
N2.rightchild = N5
N6 = TreeNode("N6")
N7 = TreeNode("N7")
N3.leftchild = N6
N3.rightchild = N7
N8 = TreeNode("N8")
N9 = TreeNode("N9")
N4.leftchild = N8
N4.rightchild = N9
N10 = TreeNode("N10")
N5.leftchild = N10
newnode = TreeNode("N11")
print(insertnode(newnode, N1))
# Insertion Success: {'parentNode': 'N5', 'position': 'Right'}





# deletetion 
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None



def deletenode(nodetodelete, rootnode=None):
    if rootnode is None:
        return "BT is empty. Nothing to delete"
    else:
        deepnode_parent = ""
        deepest_node = ""
        deepest_node_postition = ""
        customqueue = Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            poppedRootNode = customqueue.dequeue()
            if poppedRootNode.val.leftchild:
                customqueue.enqueue(poppedRootNode.val.leftchild)
                deepnode_parent = poppedRootNode
                deepest_node_postition = "leftchild"
                deepest_node = poppedRootNode.val.leftchild
            if poppedRootNode.val.rightchild:
                customqueue.enqueue(poppedRootNode.val.rightchild)
                deepnode_parent = poppedRootNode
                deepest_node_postition = "rightchild"
                deepest_node = poppedRootNode.val.rightchild
        #replacing deleted node value with deepest node value
        nodetodelete.data = deepest_node.data
        deepnode_parent.deepest_node_postition = None
        return "Deletion successful"
