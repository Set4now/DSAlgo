class BinaryTree:
    def __init__(self, size) -> None:
        self.innerlist = [None] * size
        self.maxsize = size
        self.lastusedIndex = 0 # track the last item's index

    def insertNode(self, val):
        if self.innerlist[self.lastusedIndex + 1] == self.maxsize:
            return "BT is full."
        self.innerlist[self.lastusedIndex + 1] = val
        self.lastusedIndex += 1
        return "Insertion Successfull."

    def searchNode(self, nodeValue):
        for i in range(len(self.innerlist)):
            if self.innerlist[i] == nodeValue:
                return "Node Found"
        return "BT does not have this node"
    
    def _preOrderTraversal(self, index, tempview=None):
        # Space | Time O(N)
        if tempview is not None:
            if index < len(self.innerlist):
                if self.innerlist[index] == None:
                    return
                else:
                    # we could print here as well, but instead
                    # appending it to a list for a better view later
                    tempview.append(self.innerlist[index])
                    self._preOrderTraversal((index * 2), tempview)
                    self._preOrderTraversal((index * 2) + 1, tempview)

    def getpreorderview(self):
        # temp_view is just being used for a nice view
        # N1-->N2-->N4-->N8-->N9-->N5-->N3-->N6-->N7
        temp_view = []
        self._preOrderTraversal(1, temp_view)
        return "-->".join([str(x) if type(x) == int else x for x in temp_view ])

    def _inOrderTraversal(self, index, tempview=None):
        # Space | Time O(N)
        if tempview is not None:
            if index < len(self.innerlist):
                if self.innerlist[index] == None:
                    return
                else:
                    self._inOrderTraversal((index * 2), tempview)
                    tempview.append(self.innerlist[index])
                    self._inOrderTraversal((index * 2) + 1, tempview)
    
    def getinporderview(self):
        # temp_view is just being used for a nice view
        # N8-->N4-->N9-->N2-->N5-->N1-->N6-->N3-->N7
        temp_view = []
        self._inOrderTraversal(1, temp_view)
        return "-->".join([str(x) if type(x) == int else x for x in temp_view ])

    def _postordertraversal(self, index, tempview=None):
        # Space | Time O(N)
        if tempview is not None:
            if index < len(self.innerlist):
                if self.innerlist[index] == None:
                    return
                else:
                    self._postordertraversal((index * 2), tempview)
                    self._postordertraversal((index * 2) + 1, tempview)
                    tempview.append(self.innerlist[index])
    def getpostorderview(self):
        # temp_view is just being used for a nice view
        # N8-->N9-->N4-->N5-->N2-->N6-->N7-->N3-->N1
        temp_view = []
        self._postordertraversal(1, temp_view)
        return "-->".join([str(x) if type(x) == int else x for x in temp_view ])

    def getleveorder(self):
        # Time O(N)
        # since we are storing them as sequentically while inserting
        # so level order is just a normal list iteration of all the elements
        # N1-->N2-->N3-->N4-->N5-->N6-->N7-->N8-->N9
        temp_view = []
        for index in range(1, self.lastusedIndex + 1):
           # print (self.innerlist[index])
           temp_view.append(self.innerlist[index])
        return "-->".join([str(x) if type(x) == int else x for x in temp_view ])

    def deletenode(self, nodevalue):
        # Time - O(N) | Space O(1)
        # Get the deepest node using lastused index
        # replace node to be deleted value with deepest node value
        # delet the last node
        if self.lastusedIndex == 0:
            return "There are no nodes to delete"
        for index in range(1, self.lastusedIndex + 1):
            if self.innerlist[index] == nodevalue:
                self.innerlist[index] = self.innerlist[self.lastusedIndex]
                self.innerlist[self.lastusedIndex] = None
                self.lastusedIndex -= 1
                return "Node deleted successfully"
        return "Node not found"

    def deleteTree(self):
        self.innerlist = None
        return "Tree deleted successfull"

bt = BinaryTree(11)
bt.insertNode("N1")
bt.insertNode("N2")
bt.insertNode("N3")
bt.insertNode("N4")
bt.insertNode("N5")
bt.insertNode("N6")
bt.insertNode("N7")
bt.insertNode("N8")
bt.insertNode("N9")

print(bt.getpreorderview())
#N1-->N2-->N4-->N8-->N9-->N5-->N3-->N6-->N7
print(bt.getinporderview())
#N8-->N4-->N9-->N2-->N5-->N1-->N6-->N3-->N7
print(bt.getpostorderview())
# N8-->N9-->N4-->N5-->N2-->N6-->N7-->N3-->N1
print(bt.getleveorder())
# N1-->N2-->N3-->N4-->N5-->N6-->N7-->N8-->N9
print(bt.deletenode("N9"))
# Node deleted successfully