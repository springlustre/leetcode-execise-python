def isValid(inputstr):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in inputstr:
                if len(stack)==0:
                        stack.append(x)
                else:
                        temp = stack.pop()
                        if (temp=="{" and x=="}") or (temp=="[" and x=="]") or (temp=="(" and x==")") :
                                continue
                        else:
                                stack.append(temp)
                                stack.append(x)
        if(len(stack)==0):
                return True
        else:
                return False

a = isValid("([])(){]}")
print(a)
    
