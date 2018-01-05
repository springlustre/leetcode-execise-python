def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    a = [i for i in range(1,n+1)]

    def myFunc(n,start,k):
        if k==1:
            res = []
            for i in range(start,n+1):
                res.append([i])
            return res
        else:
            res = []
            for i in range(start,n):
                x = [i]
                for r in myFunc(n,i+1,k-1):
                    t = x[:]
                    t.extend(r)
                    res.append(t)
            return res

    return myFunc(n,1,k)

a = combine(20,16)
print(a)
    
