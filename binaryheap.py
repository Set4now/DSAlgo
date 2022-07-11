class Heap:
    def __init__(self, size):
        # we don't store anythin at index 0, adding increasing size of arry by 1 (replacement of 0)
        self.customList = (size+1) * [None]
        # heapSize stores the last used index at well
        self.heapSize = 0
        self.maxSize = size + 1

# return the first item from list 
def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

# size of arr of fillef elements
def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# level Order traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapfify(heap, index, heaptype):
    
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heaptype == "Min":
        print("heapify")
        if heap.customList[parentIndex] > heap.customList[index]:
            #print ("Heapmodified: parent child swapped: {} {}".format(heap.customList[parentIndex], heap.customList[index]))
            temp = heap.customList[index]
            heap.customList[index] = heap.customList[parentIndex]
            heap.customList[parentIndex] = temp
        heapfify(heap, parentIndex, heaptype)
    if heaptype == "Max":
        if heap.customList[parentIndex] < heap.customList[index]:
            #print ("Heapmodified: parent child swapped: {} {}".format(heap.customList[parentIndex], heap.customList[index]))
            temp = heap.customList[index]
            heap.customList[index] = heap.customList[parentIndex]
            heap.customList[parentIndex] = temp
        heapfify(heap, parentIndex, heaptype)
    

def insertNode(heap, nodevalue, mintype):
    if heap.heapSize + 1 == heap.maxSize:
        return "Binary Heap is already Full!."
    newnodeindex = heap.heapSize + 1
    heap.customList[newnodeindex] = nodevalue
    heap.heapSize += 1
    heapfify(heap, newnodeindex, mintype)
    #print ("value inserted successfully")

heap = Heap(8)
insertNode(heap, 5, "Min")
insertNode(heap, 10, "Min")
insertNode(heap, 20, "Min")
insertNode(heap, 30, "Min")
insertNode(heap, 40, "Min")
insertNode(heap, 50, "Min")
insertNode(heap, 60, "Min")

levelOrderTraversal(heap)
insertNode(heap, 1, "Min")
levelOrderTraversal(heap)

def heapifyextract(rootnode, index, heaptype):
    leftchildindex = int(index * 2 )
    rightchildindex = int((index * 2) + 1 )
    swapchildindex = 0
    #base condition 
    if rootnode.heapSize < leftchildindex:
        return 

    # node has only one child (left) heapsize always maintains the last used/stored index
    elif rootnode.heapSize == leftchildindex:
        if heaptype == "Min":
            if rootnode.customList[index] > rootnode.customList[leftchildindex]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[leftchildindex]
                rootnode.customList[leftchildindex] = temp
            return
        if heaptype == "Max":
            if rootnode.customList[index] < rootnode.customList[leftchildindex]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[leftchildindex]
                rootnode.customList[leftchildindex] = temp
            return
    # node has both left and right child
    else: 
        if heaptype == "Min":
            if rootnode.customList[leftchildindex] < rootnode.customList[rightchildindex]:
                swapchildindex = leftchildindex
            else:
                swapchildindex = rightchildindex
            if rootnode.customList[index] > swapchildindex:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[swapchildindex]
                rootnode.customList[swapchildindex] = temp
        else:
            if rootnode.customList[leftchildindex] > rootnode.customList[rightchildindex]:
                swapchildindex = leftchildindex
            else:
                swapchildindex = rightchildindex
            if rootnode.customList[index] < swapchildindex:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[swapchildindex]
                rootnode.customList[swapchildindex] = temp
    heapifyextract(rootnode, swapchildindex, heaptype)

def extractfromheap(rootnode, heapType):
    if rootnode.heapSize == 0:
        return 
    extractedNode = rootnode.customList[1]
    nodereplacingroot = rootnode.customList[rootnode.heapSize]
    rootnode.customList[1] = nodereplacingroot
    rootnode.customList[rootnode.heapSize] = None
    rootnode.heapSize -= 1
    heapifyextract(rootnode, 1, heapType)
    return extractedNode

heap = Heap(8)
insertNode(heap, 5, "Min")
insertNode(heap, 10, "Min")
insertNode(heap, 20, "Min")
insertNode(heap, 30, "Min")
insertNode(heap, 40, "Min")
insertNode(heap, 50, "Min")
insertNode(heap, 60, "Min")

# levelOrderTraversal(heap)
insertNode(heap, 1, "Min")
levelOrderTraversal(heap)

print ("Extracting")
extractfromheap(heap, "Min")
levelOrderTraversal(heap)

print ("Extracting")
extractfromheap(heap, "Min")
levelOrderTraversal(heap)