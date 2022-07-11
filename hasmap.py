


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
    def add(self, key, val):
        node = Node(key, val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current_tail = self.tail
            current_tail.next = node
            self.tail = node
    def search(self, key):
        cur = self.head
        found_node = None
        while cur:
            if cur.key == key:
                found_node = cur
                break
            cur = cur.next
        return found_node
    def delete(self, key):
        if self.head:
            if self.head.key == key and self.tail.key == key:
                self.head = None
                self.tail = None
            elif self.head.key == key:
                newHead = self.head.next
                self.head = newHead
            elif self.tail.key == key:
                cur_head = self.head
                prev_node = None 
                while cur_head.next is not None:
                    prev_node = cur_head
                    cur_head = cur_head.next 
                prev_node.next = None
                self.tail = prev_node
            else:
                cur_head = self.head
                while cur_head:
                    if cur_head.next.key == key:
                        cur_head.next = cur_head.next.next
                        break
                    cur_head = cur_head.next
            return True
        return False 
    def printAll(self):
        temp = []
        cur = self.head
        while cur:
            temp.append(cur.key)
            cur = cur.next
        return "->".join([str(i) for i in temp])
class HashMap:
    '''A custom HashMap using chain Addressing using Linked list'''

    # defailt size of internal array
    MAP_SIZE = 10

    def __init__(self) -> None:
        self.container = [None] * self.MAP_SIZE

    def gethashValue(self, key):
        if type(key) is int:
            return key % self.MAP_SIZE
        if type(key) is str:
            total = 0
            for char in key:
                total += ord(char)
            return total % self.MAP_SIZE
    def insert(self, key, val):
        hashVal = self.gethashValue(key)
        if self.container[hashVal] is None:
            ll = LinkedList()
            ll.add(key, val)
            self.container[hashVal] = ll 
        else:
            # check if key already exist
            ll = self.container[hashVal]
            node = ll.search(key)
            # if key already exists, update its value
            if node:
                node.val = val
            else: # new key, so insert
                ll.add(key, val)

    def get(self, key):
        hashVal = self.gethashValue(key)
        ll = self.container[hashVal]
        node = ll.search(key)
        if node:
            return node.val
        raise KeyError("Key does not exists.")

    def delete(self, key):
        hashVal = self.gethashValue(key)
        ll = self.container[hashVal]
        node = ll.search(key)
        if node:
            return ll.delete(key)
        raise KeyError("Key does not exists.")

    def _getAllkeys(self):
        final_list = []
        for cell in self.container:
            if cell is not None:
                cur_head = cell.head
                while cur_head:
                    final_list.append((cur_head.key, cur_head.val))
                    cur_head = cur_head.next
        return final_list

    def __str__(self) -> str:
        return str(self._getAllkeys())

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.delete(key)

    def __len__(self):
        return len(self._getAllkeys())

    def __iter__(self):
        self.cellCount = 0
        self.lastNode = None
        return self

    def __next__(self):
        if self.cellCount < len(self.container):
            if self.container[self.cellCount] is not None:
                if self.lastNode is None:
                    curhead = self.container[self.cellCount].head
                    keyVal = curhead.key, curhead.val
                    self.lastNode = curhead.next
                    if not self.lastNode:
                        self.cellCount += 1
                    return keyVal
                else:
                    keyVal = self.lastNode.key, self.lastNode.val
                    if self.lastNode.next:
                        self.lastNode = self.lastNode.next
                    else:
                        self.cellCount += 1
                    return keyVal
            else:
                self.cellCount += 1
                return self.__next__()
        else:
            raise StopIteration

# a = HashMap()
# # a.insert("suman", 31)
# a.insert("suman", 34) #updating suman
# a.insert("Sunetra", 28)
# a.insert("Superman", 80)
# a["xxx"] = 1000 # __setitem__
# # print(a)
# # print(len(a))

# for i in a:
#     print (i)
# [('xxx', 1000), ('SuperMan', 50), ('Superman', 80), ('suman', 34), ('Sunetra', 28)]


def checkSameSet(a1, a2):
    if len(a1) != len(a2):
        return False
    a1chars = {}
    for i in a1:
        if i not in a1chars:
            a1chars[i] = 1
        else:
            a1chars[i] += 1
    for j in a2:
        if j in a1chars:
            a1chars[j] -= 1
        else:
            a1chars[j] = 1 
    for k,v in a1chars.items():
        if v != 0:
            return False
    return True


a1 = [2, 5, 8, 6, 10, 2, 2]
a2 = [2, 5, 6, 8, 2, 10, 2]
# print(checkSameSet(a1, a2))
  
# pairlist = [(1,3), (2,6), (3,5), (7,4), (5,3), (8,7), (7,8)]
def checkpair(pairlist):
    pairs = {}
    for i in pairlist:
        # print(i)
        if i[1] not in pairs:
            pairs[i[0]] = i[1]
        else:
            if pairs[i[1]] == i[0]:
                print (i)
            else:
                pairs[i[0]] = i[1]
    # print(pairs)
#pairlist = [(1,3), (2,6), (3,5), (5,3), (7,4), (8,7)]
# pairlist = [(7,4), (8,7), (7,8), (3,5), (5,3)]
# checkpair(pairlist)


def pairSum(a, k):
    seen = set()
    visited = set()
    for i in a:
        if i not in seen:
            seen.add(i)
    for i in a:
        if k > i:
            diff = k - i
            if diff != i:
                if diff in seen:
                    if diff not in visited:
                        visited.add(i)
                        visited.add(diff)
                        print (i, diff)
# a = [-5, 1, -40, 20, 6, 8, 7 ]
# pairSum(a, 15)

def findPair(nums, target):
 
    # create an empty dictionary
    d = {}
 
    # do for each element
    for i, e in enumerate(nums):
 
        # check if pair (e, target - e) exists
 
        # if the difference is seen before, print the pair
        if target - e in d:
            print('Pair found', (nums[d.get(target - e)], nums[i]))
            # return
 
        # store index of the current element in the dictionary
        d[e] = i
 
    # No pair with the given sum exists in the list
    print('Pair not found')
b = [-5, 1, -40, 20, 6, 8, 7 ]
findPair(b, 15)
