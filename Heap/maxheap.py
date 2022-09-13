import json
from readline import insert_text
from traceback import print_tb


class MaxHeap:
    def __init__(self, size) -> None:
        """
        MaxHeap
        The root value > left and right child's value 
        and the above statement holds True recursively down in all the subTrees

        We will not store anything at index 0 to make the calculations of parent's
        and child index easy 

        parent = childindex // 2
        leftchild = 2 * parentindex
        rightchild = (2 * parentindex) + 1

        ===========================
        FindMax O(1)
        delete / extract max = LogN
        insert LogN

        LogN -> height of the tree
        =============================

        """
        self.heaparray = [0]
        self.heapsize = size + 1

    def bottomup(self, keyindex):
        """
        Recursive Max heapify function 
        which will keep comparing node at current index with node at its parent's index
        Swap it if its value is more than its parent ( since this is MaxHeap, the parent should be larger than the child)

        keep repeating until the index becomes the top root of the heap
        """
        parent_index = keyindex // 2
        if parent_index < 1:
            # base codition means we already reach the root, the root index starts at 1
            return 
        if self.heaparray[keyindex] > self.heaparray[parent_index]:
            self.heaparray[parent_index], self.heaparray[keyindex] = self.heaparray[keyindex], self.heaparray[parent_index]
        self.bottomup(parent_index)

    def toptobottom(self, index):
        """
        In top down we keep heapifying the root 
        untill we reach a leaf node 

        Replace parent (root) with max(leftchild, rightchild)
        Now recursively call the function on the new index (index of max of (left & right ))
        """

        
        # initially setting the max item index as index
        max_item_index = index
        
        # if there exists a left child & greater than parent
        # then replace parent index 
        leftchild_index = 2 * index
        if leftchild_index < len(self.heaparray):
            if self.heaparray[leftchild_index] > self.heaparray[max_item_index]:
                max_item_index = leftchild_index
        
        # if there exists a right child & greater than parent or left child
        # then replace parent index 
        rightchild_index =  ( 2 * index ) + 1
        if rightchild_index < len(self.heaparray):
            if self.heaparray[rightchild_index] > self.heaparray[max_item_index]:
                max_item_index = rightchild_index
        
        if max_item_index != index:
            # swapping parent with child 
            self.heaparray[max_item_index], self.heaparray[index] =  self.heaparray[index], self.heaparray[max_item_index]
            # recursive call for the child (which is now storing the initial parent value)
            self.toptobottom(max_item_index)


    def insert(self, key):
        """
        1. insert the key at the heap array
        2. Perform bottom heapify until you reach top root 
        """
        if len(self.heaparray) + 1 > self.heapsize:
            return "Heap OverFlow"
        self.heaparray.append(key)

        # Get the index where we inserted the key
        key_stored_index = len(self.heaparray)- 1

        # This will max heapfy from bottom to top at insertion
        self.bottomup(key_stored_index)

    def extract_max(self):
        """
        Extract or pop the Max element ( Root) or delete the top elememt (max /root)

        1. save the first element (root)
        2. swap the element at last index with first element (current root)
        3. remove the last element
        4. decrease the heap size by 1
        5. Perform top down heapify on the new root (step 2)
        6. return the saved original root (step 1)
        """

        if len(self.heaparray) < 1:
            return "Heap is empty"

        current_max_root = self.heaparray[1]
        last_child_index = len(self.heaparray) - 1
 
        # replacing the current root with last node
        self.heaparray[1] = self.heaparray[last_child_index]

        # delete the last node
        self.heaparray.pop(-1)

        # Decreasing heap size
        self.heapsize -= 1

        #This will max heapfy from top to bottom at extraction or deletion
        self.toptobottom(1)
        
        return current_max_root

    def peek(self):
        #print(self.heaparray)
        return self.heaparray[1] 

    def __repr__(self) -> str:
        return json.dumps([self.heaparray[i] for i in range(0, len(self.heaparray))])





h = MaxHeap(5)
h.insert(1)
h.insert(200)
h.insert(67)
h.insert(50)
h.insert(400)
#h.insert(400)


print(h.extract_max())
print(h)
print(h.extract_max())
print(h)
print(h.extract_max())
print(h)
print(h.extract_max())
print(h)
print(h.extract_max())
print(h)




