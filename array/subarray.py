def subarrcheck(arr, subarr):
    subarrindex = 0
    arrindex = 0
    for i in arr:
        if i == subarr[subarrindex]:
            print(i,subarr[subarrindex])
            subarrindex += 1
        else:
            subarrindex = 0
    # print(subarrindex)
        if subarrindex == len(subarr):
            return True
    return False

def isSubArray(A, B):
     
    # Two pointers to traverse the arrays
    i = 0; j = 0
    n = len(A)
    m = len(B)
    # Traverse both arrays simultaneously
    while (i < n and j < m):
 
        # If element matches
        # increment both pointers
        if (A[i] == B[j]):
 
            i += 1
            j += 1
 
            # If array B is completely
            # traversed
            if (j == m):
                return True
         
        # If not,
        # increment i and reset j
        else:
            i = i - j + 1
            j = 0
         
    return False



a = [1,1,1,1,1,1,1,1,1,2]
b = [1,1,1,1,1,1,2]
# c = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,12]




x = ['leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 2, 'rightnull', 1, 'rightnull']
y = ['leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 1, 'leftnull', 2, 'rightnull', 1, 'rightnull']

A = ['leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 2, 'leftnull', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
B = ['leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 'leftnull', 2, 'leftnull', 1, 1, 1, 1, 1, 1]
# print(subarrcheck(A, B))
# print(isSubArray(x, y))
# print(isSubArray(A, B))



def subarrayCheck(rootNodeList, subRootList):
    print (len(rootNodeList) - len(subRootList) + 1)
    for i in range(len(rootNodeList) - len(subRootList) + 1):
        # print(rootNodeList[i: i + len(subRootList)])
        if rootNodeList[i: i + len(subRootList)] == subRootList:
            return True
    return False
a = [1,1,1,1,1,1,1,1,1,2]
b = [1,1,1,1,1,1,2]
print(subarrayCheck(a, b))