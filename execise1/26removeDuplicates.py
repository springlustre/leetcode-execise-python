def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = 0
        if not nums:
            return 0
        
        for i in range(1,len(nums)):
                        if nums[i]!=nums[res]:
                                res+=1
                                nums[res]=nums[i]
        return res+1
        
a = removeDuplicates([0,1,2,2,3,4,4,5,6])
print(a)
