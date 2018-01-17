def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    maxI = len(nums)-1
    def myFunc(arr,i):
        if i==maxI:
            return [[arr[i]]]
        else:
            x = arr[i]
            res = [[x]]
            for r in myFunc(arr,i+1):
                t = [x]
                t.extend(r)
                res.append(r)
                res.append(t)
            return res

    r = myFunc(nums,0)
    r.insert(0,[])
    return r

a = subsets([1,2,3])
print(a)
    
