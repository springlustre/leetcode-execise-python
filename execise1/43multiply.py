def multiply(num1,num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        len1 = len(num1)
        len2 = len(num2)
        for i in range(len1):
                x = 1
                for k in range(i):
                        x = x*10
                a = (ord(num1[len1-i-1]) - ord('0'))*x
                
                for j in range(len2):
                        x = 1
                        for k in range(j):
                                x = x*10
                        b = x*(ord(num2[len2-j-1])-ord('0'))
                        res+=a*b
                        
                
        return  str(res)

a = multiply("19","9")
print(a)
    
