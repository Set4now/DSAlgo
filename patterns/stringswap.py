from locale import currency


def swap(word, i):
    final = []
    j = 0
    while j < len(word):
        charlist = list(word)
        charlist[i], charlist[j] = charlist[j], charlist[i]
        final.append("".join(charlist))
        j += 1

    return final

def permutation(word, i, finallist):
    if i == len(word) - 1:
        return finallist
    temp = swap(word, i)
    finallist.extend([ word for word in temp if word not in finallist])
    for pattern in temp:
        permutation(pattern, i+1, finallist)
    return finallist

# print(permutation("ABCDE", 0, []))




class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None 

    def addnode(self, node):
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            currtail = self.tail
            currtail.next = node
            self.tail = node

    def show(self):
        currenode = self.head
        ll = []
        while currenode:
            ll.append(currenode.data)
            currenode = currenode.next
        print ("-->".join(ll))
    
    def reverse(self):
        prev = None
        currhead = self.head
        while currhead:
            nextnode = currhead.next
            currhead.next = prev 
            prev = currhead
            currhead = nextnode
        self.head = prev
    



        

a = Node("a")
b = Node("b")
c = Node("c")  
d = Node("d")  
e = Node("e")  

ll = LL()
ll.addnode(a)
ll.addnode(b)
ll.addnode(c)
ll.addnode(d)
ll.addnode(e)

# ll.show()

ll.reverse()

ll.show()
