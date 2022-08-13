a = [[1,0,1],
     [1,1,0], 
     [1,0,0]]


a = [
    [0,1,0,0,1,1,1,1],
    [0,0,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0]
]


row = len(a)
col = len(a[0])
b = [[0] * col for _ in a]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 1:
            # print(i,j)
            b[i][j] = 1
            # print(b)

print(b)

