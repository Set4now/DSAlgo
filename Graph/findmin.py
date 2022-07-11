a = {'A': 100, 'B': 3, 'C': 5, 'D': float('inf'), 'E': float('inf'), 'F': float('inf'), 'G': float('inf')}

v = float('inf')
node = ""
for n, distance in a.items():
    if distance < v:
        node = n
        v = distance

print(node)
print(v)