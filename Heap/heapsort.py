class MaxHeap:
    def __init__(self, size) -> None:
        self.heaparray = [0]
        self.heapsize = size + 1

    def insert(self, key):
        # Heap is full
        if len(self.heaparray) + 1 > self.heapsize:
            return False
        self.heaparray.append(key)
        last_inserted_index = len(self.heaparray) - 1

        self.bottomup_heapify(last_inserted_index)

    def bottomup_heapify(self, index):
        parent_index = index // 2
        if parent_index < 1:
            return
        if self.heaparray[index] > self.heaparray[parent_index]:
            self.heaparray[index], self.heaparray[parent_index] = self.heaparray[parent_index], self.heaparray[index]
        self.bottomup_heapify(parent_index)

    def toptobottom_heapify(self, index, ignoreindex):
        """
        Heapify from top to bottom except child at ignoreindex
        Since that will store the max number, which will be useful since we 
        are using this algo to sort the arr in ascending order
        """
        max_item_index = index

        leftchild_index = index * 2
        if leftchild_index < len(self.heaparray) and leftchild_index < ignoreindex:
            if self.heaparray[leftchild_index] > self.heaparray[max_item_index]:
                max_item_index = leftchild_index
        
        rightchild_index =  (index * 2) + 1
        if rightchild_index < len(self.heaparray) and rightchild_index < ignoreindex:
            if self.heaparray[rightchild_index] > self.heaparray[max_item_index]:
                max_item_index = rightchild_index

        if max_item_index != index:
            self.heaparray[index], self.heaparray[max_item_index] = self.heaparray[max_item_index], self.heaparray[index]
            self.toptobottom_heapify(max_item_index, ignoreindex)

    def heapsort(self):
        """
        This is similar to extract max (deleting the top root with max value )
        Once we swap it with the last element in the heap array
        we will not delete it, we would rather keep it in its swapped place

        Since in the sorted array (ascending) , the largest elements will always be at the end

        We will just tell toptobottom_heapify function to ignore the child at this index
        while heapifying from top to bottom 

        Time: N(logN)

        """

        last_child_index = len(self.heaparray) - 1

        while last_child_index > 1:
            self.heaparray[1], self.heaparray[last_child_index] = self.heaparray[last_child_index], self.heaparray[1]
            self.toptobottom_heapify(1, last_child_index)
            last_child_index -= 1

        # The first item at index 0 is 0, since we don't use index 0 in our heap
        # So return the elements from index 1
        sorted_list = [ self.heaparray[i] for i in range(1, len(self.heaparray))]
        return sorted_list


def heap_sort(arr):
    h = MaxHeap(len(arr))
    for i in arr:
        h.insert(i)
    return h.heapsort()


arr = [10,9,8,7,6,5,4,3,2,1,0]
print(heap_sort(arr))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
