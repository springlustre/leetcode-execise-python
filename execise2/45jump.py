def jump(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
                return 0
        cur = 0 #当前最远
        last = 0 #上次最远
        step = 0

        for i in range(len(nums)):
                if i > cur:#无论如何都到不了终点
                        return -1
                if i > last:# 需要进行下一次跳跃
                        last = cur
                        step +=1
                cur = cur if cur>nums[i]+i else nums[i]+i
        
        if cur>=len(nums)-1:
                return step
        else:
                return -1

a = jump([2,3,1,1,4])
print(a)
    
