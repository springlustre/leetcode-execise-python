def numTrees(n):
    """
    :type n: int
    :rtype: int
    """

    # catch = {}
    # def myNum(start,end):
    #     if start>=end:
    #         return 1
    #     k = str(start)+","+str(end)
    #     if k in catch:
    #         return catch[k]
    #     else:
    #         res = 0
    #         for i in range(start,end+1):
    #             l = myNum(start,i-1)
    #             k = str(start)+","+str(i-1)
    #             catch[k] = l
    #             r = myNum(i+1,end)
    #             k = str(i+1)+","+str(end)
    #             catch[k] = r
    #             res += l*r
    #         return res
    #
    # if n<1:
    #     return 0
    # return myNum(1,n)
    # 0  1
    # 1   1
    # 2  2
    # 3
    v = [0] * (n+1)
    v[0] = 1
    v[1] = 1
    if n<2:
        return 1
    v[2] = 2
    for  k in range(3,n+1):
        r = 0
        for i in range(1,k+1):
            r+=v[i-1]*v[k-i]
        v[k] = r
    return v[n]

a = numTrees(1)
print(a)