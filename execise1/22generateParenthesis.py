##此处用的递归，此题也可以用回溯解决
def insert(s,i,new):
        return s[:i]+new+s[i:]
def genByStep(l,n):
        if n!=0:
                s = set()
                for x in l:
                        for i in range(len(x)):
                                s.add(insert(x,i,"()"))
                                #print(n,list(s))
                return genByStep(s,n-1)
        else:
                res = list(l)
                #print(len(res))
                return res
def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
                return []
        else:
                init = set()
                init.add("()")
                return genByStep(init,n-1)

a = generateParenthesis(4)
print(a)
    
