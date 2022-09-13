from heapq import heappush, heappop

h = []
heappush(h, (5, "node1"))
heappush(h, (4, "node2"))
heappush(h, (3, "node3"))
heappush(h, (2, "node4"))
heappush(h, (1, "node5"))

print(heappop(h))
print(heappop(h))
print(heappop(h))
print(heappop(h))
print(heappop(h))