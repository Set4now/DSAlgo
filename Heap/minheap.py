import json
from readline import insert_text
from traceback import print_tb


class MinHeap:
    def __init__(self, size) -> None:
        """
        MinHeap
        The root value < left and right child's value 
        and the above statement holds True recursively down in all the subTrees

        We will not store anything at index 0 to make the calculations of parent's
        and child index easy 

        parent = childindex // 2
        leftchild = 2 * parentindex
        rightchild = (2 * parentindex) + 1



        """
        self.heaparray = [0]
        self.heapsize = size + 1

    def bottomup(self, keyindex):
        """
        Recursive Min heapify function 
        which will keep comparing node at current index with node at its parent's index
        Swap it if its value is less than its parent ( since this is MinHeap, the parent should be smaller than the childs)

        keep repeating until the index becomes the top root of the heap
        """
        parent_index = keyindex // 2
        if parent_index < 1:
            # base codition means we already reach the root, the root index starts at 1
            return 
        if self.heaparray[keyindex] < self.heaparray[parent_index]:
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
        
        leftchild_index = 2 * index
        rightchild_index =  ( 2 * index ) + 1
        
        # if there exists a left child & smaller than parent
        # then replace parent index 

        min_item_index = index
        
        if leftchild_index < len(self.heaparray) and index >= 1:
            if self.heaparray[leftchild_index] < self.heaparray[min_item_index]:
                min_item_index = leftchild_index
        
        # if there exists a right child & smaller than parent or left child
        # then replace parent index 
        
        if rightchild_index < len(self.heaparray) and index >= 1:
            if self.heaparray[rightchild_index] < self.heaparray[min_item_index]:
                min_item_index = rightchild_index
        
        if min_item_index != index:
            # swapping parent with child 
            self.heaparray[index], self.heaparray[min_item_index] = self.heaparray[min_item_index], self.heaparray[index]
            # recursive call for the child (which is now storing the initial parent value)
            self.toptobottom(min_item_index)


    def insert(self, key):
        """
        1. insert the key at the heap array
        2. Perform bottom heapify until you reach top root 
        """
        if len(self.heaparray) + 1 > self.heapsize:
            return "Heap OverFlow"
        self.heaparray.append(key)

        # Get the index where we inserted the key
        key_stored_index = len(self.heaparray) - 1

        # This will max heapfy from bottom to top at insertion
        self.bottomup(key_stored_index)

    def extract_min(self):
        """
        Extract or pop the Max element ( Root) or delete the top elememt (max /root)

        1. save the first element (root)
        2. swap the element at last index with first element (current root)
        3. remove the last element
        4. decrease the heap size by 1
        5. Perform top down heapify on the new root (step 2)
        6. return the saved original root (step 1)
        """

        if len(self.heaparray) == 1:
            return "Heap is empty"

        current_min_root = self.heaparray[1]
        last_child_index = len(self.heaparray) - 1
 
        # replacing the current root with last node
        self.heaparray[1] = self.heaparray[last_child_index]

        # delete the last node
        self.heaparray.pop()

        # Decreasing heap size
        self.heapsize -= 1

        #This will max heapfy from top to bottom at extraction or deletion
        self.toptobottom(1)
        
        return current_min_root

    def peek(self):
        #print(self.heaparray)
        return self.heaparray[1] 

    def __repr__(self) -> str:
        return json.dumps([self.heaparray[i] for i in range(0, len(self.heaparray))])






h = MinHeap(5)

# data = [100, 77, 34, 2, 90]
# for i in data:
#     h.insert(i)
# #print(h.peek())
# #print(h.extract_min())


h.insert(1)
h.insert(200)
h.insert(67)
h.insert(50)
h.insert(400)

print(h)
#h.insert(400)
# print(h.peek())

print(h.extract_min())
print(h)
print(h.extract_min())
print(h)
print(h.extract_min())
print(h)
print(h.extract_min())
print(h)
print(h.extract_min())
print(h)
# print(h.peek())