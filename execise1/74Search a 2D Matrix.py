def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row = len(matrix)
    if row ==0:
        return False
    col = len(matrix[0])
    i = row-1
    j = 0
    while i>=0 and j <col:
        x = matrix[i][j]
        if x==target:
            return True
        elif target<x:
            i-=1
        else:
            j+=1

    return False

a = searchMatrix([
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
],55)
print(a)
    
