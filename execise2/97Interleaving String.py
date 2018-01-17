def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    # dp
    # l1 = len(s1)
    # l2 = len(s2)
    # l3 = len(s3)
    # if l1+l2!=l3:
    #     return False
    # t = [[False]*(l2+1)]*(l1+1)
    # t[0][0] = True
    #
    # for i in range(0,l1+1):
    #     for j in range(0,l2+1):
    #         if j==0:
    #             if i>0:
    #                 t[i][j] = t[i-1][j] and s1[i-1]==s3[i-1]
    #         elif i==0:
    #             if j>0:
    #                 t[i][j] = t[i][j-1] and s2[j-1]==s3[j-1]
    #         else:
    #             t[i][j] =  (t[i-1][j] and s1[i-1]==s3[i+j-1])  or (t[i][j-1] and s2[j-1]==s3[i+j-1])
    #         # print(i,j,t[i][j])
    # return t[l1][l2]

    # dfs
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if l1+l2!=l3:
        return False
    catch = {}
    def myFunc(i,j,k):
        key = str(i)+","+str(j)
        if key in catch:
            return catch[key]
        if k>=l3:
            return True
        res = (i<l1 and s1[i]==s3[k] and myFunc(i+1,j,k+1)) or  \
              (j<l2 and s2[j]==s3[k] and myFunc(i,j+1,k+1))
        catch[key] = res
        return res
    return myFunc(0,0,0)

a = isInterleave("aabcc","dbbca","aadbbcbcac")
print(a)