def grayCode(n):
    """
    :type n: int
    :rtype: List[int]
    """

    def powOf2(n):
        res = 1
        for i in range(n):
            res*=2
        return res

    # def myGray(n,f):
    #     if n==1:
    #         if f==0:
    #             return [0,1]
    #         else:
    #             return [1,0]
    #     else:
    #         res = []
    #         if f==0:
    #             for x in myGray(n-1,0):
    #                 res.append(x)
    #             h = pow(2,n-1)
    #             for x in myGray(n-1,1):
    #                 res.append(x+h)
    #         else:
    #             h = pow(2,n-1)
    #             for x in myGray(n-1,0):
    #                 res.append(x+h)
    #             for x in myGray(n-1,1):
    #                 res.append(x)
    #         return res

    if n==0:
        return [0]
    res = [0,1]
    if n==1:
        return res
    for i in range(1,n):
        h = pow(2,i)
        t = res[:]
        t.reverse()
        for x in t:
            res.append(x+h)

    # return myGray(n,0)
    return res

a = grayCode(0)
print(a)