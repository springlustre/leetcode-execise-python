def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    # def myDecode(s,n):
    #     if n==0:
    #         return 0
    #     if n==1:
    #         if s=="0":
    #             return 0
    #         else:
    #             return 1
    #     elif n==2:
    #         if s[0]=="0":
    #             return 0
    #         if int(s) <=26:
    #             if s[1]=="0":
    #                 return 1
    #             else:
    #                 return 2
    #         else:
    #             if s[1]!="0":
    #                 return 1
    #             else:
    #                 return 0
    #     else:
    #         if s[0]=="0":
    #             return 0
    #         else:
    #             r = myDecode(s[1:],n-1) + (myDecode(s[2:],n-2) if int(s[:2])<27 else 0)
    #             return r
    # return myDecode(s,len(s))

    length = len(s)
    if length==0:
        return 0
    elif length==1:
        if s[0]=="0":
            return 0
        else:
            return 1
    arr = [0]*(length+1)
    if  s[-1]=="0":
        arr[-2] = 0
    else:
        arr[-2] = 1
    arr[-1] = 1
    i = length-2
    while i>=0:
        x = s[i]
        if x=="0":
            arr[i] = 0
            i-=1
            continue
        t = 0
        if int(x+s[i+1])<27:
            t = arr[i+2]
        arr[i] = arr[i+1]  + t
        i-=1
    return arr[0]
# 1  2  3  4
#     3    2    1    1  1
#
# 234  2
#
# 34  1



a = numDecodings("10")
# a = numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
print(a)
    
