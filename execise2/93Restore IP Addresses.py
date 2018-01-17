def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def myIp(s,n):
        lens = len(s)
        if n==1:
            if lens>3 or int(s)>255 or (lens>1 and s[0]=="0"):
                return []
            else:
                return [s]
        else:
            res = []
            for i in range(1,4):
                ts = s[:i]
                ts2 = s[i:]
                if int(ts)<256 and len(ts2)>=n-1 and (i<2 or i>1 and ts[0]!="0"):
                    for r in myIp(ts2,n-1):
                        res.append(ts+"."+r)
            return res
    if len(s)<4:
        return []

    return myIp(s,4)

a = restoreIpAddresses("0000")


print(a)
    
