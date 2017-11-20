def calNext(str):
        next = []
        next.append(-1)
        k = -1
        for q in range(1,len(str)):
                while k>-1 and str[k+1]!=str[q]:
                        k = next[k] #向上回溯
                if str[k+1]==str[q]: #上次的最大前缀的下一位等于当前位
                        k = k+1
                next.append(k) 
        return next


def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        nextList = calNext(needle)
        i = 0
        j = -1
        while i < len(haystack):
                while j >-1 and haystack[i]!=needle[j+1]:
                        j = nextList[j]
                if haystack[i]==needle[j+1]:
                        j = j+1
                
                if j==len(needle)-1:
                        return i-len(needle)+1
                i = i+1
                                
                        
        return -1    
a = strStr("qweer","er")
print(a)
