class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None

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

def deletenode(nodetodelete, rootnode=None):
    if rootnode is None:
        return "BT is empty. Nothing to delete"
    else:
        '''
            Using level order to find the deepest node
            deepest node will be last dequeued node from queue
            We are storing three reference which we will use later
            a. deepest node
            b. parent node of the deepest node
            c. postion of deepest node (left or child) from the parent node
        '''
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
        if nodetodelete.leftchild:
            print ("new parent of {} is {}".format(nodetodelete.leftchild.data, nodetodelete.data))
        if nodetodelete.rightchild:
            print ("new parent of {} is {}".format(nodetodelete.rightchild.data, nodetodelete.data))
        return "Deletion successful"

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

print(deletenode(N3, N1))
# new parent of N6 is N9
# new parent of N7 is N9
# Deletion successful