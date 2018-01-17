def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # length = len(nums)
    # def mySub(k):
    #     if k == length-1:
    #         return [str(nums[k])]
    #     else:
    #         h = nums[k]
    #         s = str(h)
    #         res = set()
    #         res.add(s)
    #         print("res",res)
    #         for x in mySub(k+1):
    #                 res.add(x)
    #                 print(x)
    #                 r = s+","+x
    #                 res.add(r)
    #
    #         print(list(res))
    #         return list(res)
    # # res = []
    # res = list(map(lambda x:list(map(lambda y:int(y),x.split(","))), mySub(0)))
    # print(res)
    # # for i in mySub(0):
    # #     r = []
    # #     for j in i.split(","):
    # #         r.append(int(j))
    # #     res.append(r)
    #
    # res.append([])
    # return res

    nums.sort()
    res = []
    if not nums:
        return res
    last = nums[0]-1
    cnt = 0
    for x in nums:
        print("x",x)
        if x==last:
            lastLen = len(res)
            for r in res[cnt:]:
                t = r[:]
                t.append(x)
                res.append(t)
            cnt = lastLen
        else:
            cnt = len(res)
            for r in res[:]:
                t = r[:]
                t.append(x)
                res.append(t)
            res.append([x])
        last = x
        print(res)
    res.append([])
    return res
# 1
# 1 12  2
# 1  12 2   122 22
# 1  12 2   122 22  1222 222

a = subsetsWithDup([1,1,2,2,2])
print(a)