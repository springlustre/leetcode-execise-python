def longestValidParentheses(s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        cnt = 0
        record = []
        for i in range(0,len(s)):
                record.append(0)
        for i in range(1,len(s)):
                x = s[i]
                if x == ')':#遇到右括号才进行以下操作
                        if s[i-1]=='(':
                                old = record[i-2] if i>1 else 0
                                record[i] = old+2
                        else:#如果上一个还是右括号，则检查之前匹配的上一个
                                pre = i - record[i-1] -1
                                if pre>=0 and s[pre]=='(':
                                        pre2 = i - record[i-1]-2
                                        t = 0 if pre2<0 else record[pre2]
                                        record[i] = record[i-1]+t+2
                res = res if res>record[i] else record[i]
                                
        return res
        
a = longestValidParentheses("(()()(())))")
print(a)
    
