def countAndSay(n):
        """
        :type n: int
        :rtype: str
        """

        def say(s):
                c = 0
                res = ""
                for i in range(0,len(s)):
                        if i==0:
                                c +=1
                        else:        
                                if s[i] == s[i-1]:
                                        c+=1
                                else:
                                        res = res + str(c) + s[i-1]
                                        c = 1
                        if i == len(s)-1:
                                res = res + str(c) + s[i]
                return res

        res = "1"
        for i in range(n-1):
                res = say(res)
                #print(res)
                
        return res

a = countAndSay(6)

    
