def lengthOfLastWord(s):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = 0
        temp = s[::-1]
        for x in temp:
                if x==' ':
                        if res>0:
                                return res
                else:
                        res+=1

        return  res

a = lengthOfLastWord("hello world")
print(a)
    
