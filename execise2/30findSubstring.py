def findSubstring(s,words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #看了别人的解法，用的滑动窗口法，

        if words==[]:
                return []
        res = []
        l1 = len(words[0])
        l2 = len(words)
        length = l1*l2
        i=0
        map = {}
        #将words的元素存储到字典
        for w in words:
                if w in map:
                        v = map[w]
                        map[w] = v+1
                else:
                        map[w] = 1
        length2 = len(s)
        while i < l1:
                cnt = 0
                left = i
                cur = {}
                for j in range(i,length2,l1):
                        w = s[j:j+l1]
                        #print(w)
                        if w in map:
                                if w in cur:
                                        cur[w] = cur[w]+1
                                else:
                                        cur[w] = 1
                                if map[w]>=cur[w]:
                                        cnt = cnt+1
                                else:
                                        while cur[w] > map[w]:
                                                temp = s[left:left+l1]
                                                if temp in cur:
                                                        cur[temp] = cur[temp] - 1
                                                        if cur[temp] < map[temp]:
                                                                cnt = cnt-1
                                                left = left + l1
                                if cnt==l2:
                                        res.append(left)
                                        #如果cur包含下一个单词，则cnt-1
                                        temp = s[left:left+l1]
                                        if temp in cur:
                                                cur[temp] = cur[temp] - 1
                                                cnt = cnt-1
                                        left = left + l1
                        else:
                                left = j+l1
                                cnt = 0
                                cur.clear()
                                #print(left)
                i = i+1
                
        return res



        
#         if words==[]:
#                 return []
#         res = []
#         l1 = len(words[0])
#         l2 = len(words)
#         length = l1*l2
#         i=0
#         map = {}
#         for w in words:
#                 if w in map:
#                         v = map[w]
#                         map[w] = v+1
#                 else:
#                         map[w] = 1
                        
#         while i < (len(s)-length+1):
#                 temp = map.copy()
#                 for j in range(0,l2):
#                         start = i+j*l1
#                         end = i+j*l1+l1
#                         w = s[start:end]
#                         if w in temp:
#                                 v = temp[w]
#                                 if v>1:
#                                         temp[w] = v-1
#                                 else:
#                                         del temp[w]
#                 if len(temp)==0:
#                         res.append(i)
#                 i = i+1
#         return res
a = findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
print(a)
    
