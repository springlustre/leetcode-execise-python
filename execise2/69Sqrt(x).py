def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """

    # high = x//2 + x%2
    # low = 0
    #
    # while low<=high:
    #     m = (low+high)//2
    #     t = m*m
    #     print(low,high)
    #     if t == x:
    #         return m
    #     elif t>x:
    #         high = m-1
    #     else:
    #         low = m+1
    #
    # return low-1

    def myFunc(x):
        if x<4:
            return 0 if x==0 else 1
        else:
            r = 2*myFunc(x//4)
            if (r+1)*(r+1)<=x:
                return r+1
            else:
                return r


    return myFunc(x)


a = mySqrt(18)
print(a)
    
