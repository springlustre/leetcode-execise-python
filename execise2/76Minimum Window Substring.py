def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    map = {}
    for i in s:
        map[i] = 0
    for i in t:
        if i in map:
            map[i] = map[i]+1
        else:
            return ""
    cnt = len(t)
    start = 0
    end = 0
    length = 0
    minStart = 0
    for x in s:
        if map[x] >0:
            cnt-=1
        map[x] = map[x]-1
        end+=1
        while cnt==0:
            print(start,end,cnt)
            if length==0 or length > (end - start):
                length = end - start
                minStart = start
            t = s[start]
            if map[t]>=0: #起始位置在t中
                cnt+=1
            map[t] = map[t]+1
            start+=1

    return s[minStart:minStart+length]




a = minWindow("bba","ab")
print(a)
    
