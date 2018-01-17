def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 132 231 213   231321 231312 231132   232113
        length = len(nums)
        index = length-1
        flag = False
        for i in range(1,length+1):
                j = length-i #j从最右边往左遍历
                if nums[j] > nums[j-1]:
                        temp = nums[j-1]
                        minus = nums[j]-nums[j-1]
                        n = j
                        #print(n,nums)
                        for m in range(j,length):
                                if nums[m]>temp: #如果比temp大
                                        x = nums[m] - temp
                                        if minus>0:
                                                if x<minus:
                                                        minus = x
                                                        n = m
                                                        
                                        else:
                                                temp = x
                                                n = m
                        #print(n)
                        t = nums[j-1]
                        nums[j-1] = nums[n]
                        nums[n] = t
                        
                        flag = True
                        k = j #下面对[k,length]排序
                        #print(nums)
                        while k <length-1:
                                for m in range(k+1,length):
                                        #print(m,k)
                                        if nums[k]>nums[m]:
                                                temp = nums[k]
                                                nums[k] = nums[m]
                                                nums[m] = temp
                                k = k+1
                        break
                elif nums[index] > nums[j]:
                        index = j
        if not flag:
                nums.sort()
        return  nums

a = nextPermutation([1,3,2])
print(a)
    
