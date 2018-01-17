def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    length = len(digits)
    res = []
    over = 0
    d = digits[-1]+1
    if d>9:
        over = d//10
        d2 = d%10
        digits[-1] = d2
    else:
        digits[-1] = d
    i = length-2
    while over>0 and i>=0:
        d = digits[i]+over
        if d>9:
            over = d//10
            d2 = d%10
            digits[i] = d2
        else:
            over = 0
            digits[i] = d
        i-=1
    if over>0:
        digits.insert(0,over)
    return digits

a = plusOne([9,9,9])
print(a)
    
