def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # def mulOf2(n):
    #     if n==0:
    #         return 1
    #     else:
    #         res = 1
    #         for i in range(n):
    #             res*=2
    #         return res
    # def conv1(x):
    #     n = len(x)-1
    #     res = 0
    #     for i in x:
    #         res += (mulOf2(n)*int(i))
    #         n-=1
    #     return res
    #
    # def conv2(x):
    #     if x==0:
    #         return "0"
    #     res = ""
    #     while x>0:
    #         res = str(x%2)+res
    #         x = x//2
    #     return res
    # c = conv1(a)+conv1(b)

    l1 = len(a)
    l2 = len(b)
    min = 0
    minus = 0
    if l1>l2:
        min = l2
        max = l1
    else:
        min = l1
        max = l2
        c = a
        a = b
        b = c
    i = 1
    over = 0
    res = ""
    while i <= min:
        c = int(a[-i]) + int(b[-i]) + over
        res = str(c%2)+res
        over = c//2
        i+=1

    while over >0 or i<=max:
        x = 0 if i > max else int(a[-i])
        c = x + over
        res = str(c%2)+res
        over = c//2
        i+=1

    return res

a = addBinary("1","0")
print(a)
    
