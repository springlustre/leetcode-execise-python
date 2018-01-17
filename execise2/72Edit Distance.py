def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    len1 = len(word1)
    len2 = len(word2)
    if len1==0:
        return len2
    if len2==0:
        return len1
    d = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    for i in range(0,len2+1):
        d[0][i] = i
    for i in range(0,len1+1):
        d[i][0] = i
    print(d)
    def myMin(x,y,z):
        t = x if x<y else y
        return t if t<z else z
    i = 0
    while i < len1:
        j=0
        while j < len2:
            k = 0 if word1[i]==word2[j] else 1
            d[i+1][j+1] = myMin(d[i][j+1]+1,d[i+1][j]+1,d[i][j]+k)
            print("i",i,"j",j,d[i+1][j+1])
            j+=1
        i+=1
    # print(d)
    return d[len1][len2]

a = minDistance("sea", "eat")
print(a)
    
