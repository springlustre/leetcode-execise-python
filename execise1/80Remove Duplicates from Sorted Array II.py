def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    m = {}
    res = 0
    for x in nums[:]:
        m[x] = m.get(x,0)+1
        print(m)
        # m[x]+=1
        if m[x] >2:
            # m[x] = 2
            # res+=1
            # else:
            nums.remove(x)
            # else:
            #     m[x] = 1
            # res+=1
    return len(nums)

a = removeDuplicates([1,1,1,1])
print(a)
    
