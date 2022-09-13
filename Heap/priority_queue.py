import json


class MinPriorityQueue:
    def __init__(self) -> None:
        """
        A Min priority Queue implementation with Min heap 
        """
        self.array = [0]
        #self.heapsize = size + 1

    def enqueue(self, key):
        self.array.append(key)
        last_key_inserted_index = len(self.array) - 1
        self._heapify_bottomup(last_key_inserted_index)

    def is_empty(self):
        return len(self.array) == 1

    def dequeue(self):
        """ Poping the Min (root) from Heap """
        if self.is_empty():
            raise Exception("Queue is empty")
        min_root = self.array[1]

        last_child_index = len(self.array) - 1
        self.array[1] = self.array[last_child_index]
        self.array.pop()
        self._heapify_toptobottom(1)
        return min_root

    def _swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def _heapify_bottomup(self, index):
        parent_index = index // 2
        if parent_index < 1:
            return
        if self.array[index] < self.array[parent_index]:
            self._swap(index, parent_index)
        self._heapify_bottomup(parent_index)
            
    def _heapify_toptobottom(self, index):
        min_index = index
        

        left_child_index = 2 * index
        if left_child_index < len(self.array) and left_child_index >= 1:
            if self.array[left_child_index] < self.array[min_index]:
                min_index = left_child_index

        right_child_index = ( 2 * index) + 1
        if right_child_index < len(self.array) and right_child_index >= 1:
            if self.array[right_child_index] < self.array[min_index]:
                min_index = right_child_index

        if min_index != index:
            #print(min_index, index)
            self._swap(index, min_index)
            self._heapify_toptobottom(min_index)

    def __repr__(self) -> str:
        return json.dumps([ self.array[i] for i in range(1, len(self.array))])  


q = MinPriorityQueue()
data = [100, 77, 34, 2, 90, 56, 78, 44]
for i in data:
    q.enqueue(i)
print(q)
# print("=====")


while not q.is_empty():
    print(q.dequeue())
    #print(q)