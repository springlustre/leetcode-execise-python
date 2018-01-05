def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n ==1:
        return 1
    if n==2:
        return 2
    s = [1,2]
    s.extend([0 for _ in range(n-2)])
    for i in range(2,n):
        s[i] = s[i-1]+s[i-2]

    return s[n-1]



a = climbStairs(4)
print(a)
    
