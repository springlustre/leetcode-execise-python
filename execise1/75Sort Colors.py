def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    start1 = length
    start2 = length
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in nums:
        if i ==0:
            cnt0+=1
        elif i==1:
            cnt1+=1
        else:
            cnt2+=1
    print(cnt0,cnt1,cnt2)
    for i in range(cnt0):
        nums[i] = 0
    for i in range(cnt0,cnt0+cnt1):
        nums[i]  = 1
    for i in range(cnt0+cnt1,cnt0+cnt1+cnt2):
        nums[i] = 2

    return nums







a = sortColors([0,2,1,2,1,0,1,2])
print(a)
    
