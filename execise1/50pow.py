def myPow(x,n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if n==0:
                return 1
        if n <0:
                n = -n
                x = 1/x
        if n%2==0:
                return myPow(x*x,n//2)
        else:
                return x*myPow(x*x,n//2)

a = myPow(2.00000,10)
print(a)
    
