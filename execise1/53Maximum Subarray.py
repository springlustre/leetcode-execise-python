def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
                return 0
        res = nums[0]
        temp = 0
        for x in nums:
                temp = temp+x
                if temp>res:
                                res = temp
                if temp<0:
                        temp = 0
                

        return  res

a = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)
    
