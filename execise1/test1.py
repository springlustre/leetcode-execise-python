def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        r = []
        length = len(nums)
        i = 0
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
                print(a,b,c)
                flag = b!=nums[j-1] and c!=nums[k+1] if j>i and k<length-1 else True
                if a+b+c==0 and flag:
                    res.append([a,b,c])
                    j = j+1
                    k = k-1
                elif a+b+c>0:
                    k = k-1
                elif a+b+c<0:
                    j = j+1
                else:
                    j = j+1
                    k = k-1

        return  res

a = threeSum([0,-4,-1,-4,-2,-3,2])
print(a)
    
