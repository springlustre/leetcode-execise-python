def isScramble(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    def myFunc(n,i,j):
        if n==1:
            return s1[i:i+n] == s2[j:j+n]
        else:
            s1


a = isScramble("rgeat","great")
print(a)

