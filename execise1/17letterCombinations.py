def letterCombinations(digists):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
               '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
               '8':['t','u','v'],'9':['w','x','y','z']}
        res  = [''] if(len(digits)>0) else []
        for i in range(len(digits)):
                k = digits[i]
                li = mapping.get(k)
                temp=[]
                for j in range(len(li)):##一个键盘上的字母
                        letter = li[j]
                        for r in range(len(res)):##之前的结果
                                o = res[r]
                                temp.append(o+letter)
                res = temp
        return res

print(letterCombinations(""))
