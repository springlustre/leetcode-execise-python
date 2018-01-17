def threeSumClosest(nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = 0
        nums.sort()
        length = len(nums)
        i = 0
        minutes = 0
        while i < length:
            i = i+1
            j = i
            k = length-1
            a = nums[i-1]
            if i>1 and nums[i-1]==nums[i-2]:
                continue
            while j<k:
                b = nums[j]
                c = nums[k]
                s = a+b+c-target
                print(a,b,c,s)
                if s==0:
                    res = target
                    return res
                elif s>0:
                    k = k-1
                    if(minutes==0 or minutes>s):
                        minutes = s
                        res = a+b+c
                else:
                    j = j+1
                    if(minutes==0 or minutes>-s):
                        minutes = -s
                        res = a+b+c

        return  res

a = threeSumClosest([0,-4,-1,-4,-2,-3,2],-2)
print(a)
    
