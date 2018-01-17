def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = []
    for i in range(1,rowIndex+2):
        r = [1]*i
        for k in range(1,i-1):
            r[k] = res[k]+res[k-1]
        res = r
    return res
