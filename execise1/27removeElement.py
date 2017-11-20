def removeDuplicates(nums,val):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = 0
        if not nums:
            return 0
        
        for i in range(len(nums)):
                        if nums[i]!=val:
                                nums[res]=nums[i]
                                res+=1
        return res
        
a = removeDuplicates([0,1,2,2,3,4,4,5,6],2)
print(a)
