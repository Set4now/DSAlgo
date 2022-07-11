class CustomQueue:
    def __init__(self) -> None:
        self.container = []

    def enque(self, key):
        self.container.append(key)

    def dequeue(self):
        popped = self.container[0]
        self.container.remove(self.container[0])
        return popped

    def isempty(self):
        return len(self.container) == 0


# a = CustomQueue()
# a.enque(1)
# a.enque(2)
# a.enque(3)

# print(a.dequeue())
# print(a.dequeue())
# print(a.dequeue())