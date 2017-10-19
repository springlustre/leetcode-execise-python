def fourSum(nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        print(nums)
        length = len(nums)
        i = 0
        j = length-1
        m = 0
        n = 0
        nextStep = 0
        while i<j-2:#i和j最小相差2
                m = i+1
                n = j-1
                a = nums[i]
                b = nums[j]
                f1 = a==nums[i-1] if i>0 else False
                f2 = b==nums[j+1] if j<length-1 else False

                if nextStep==0:
                        j = j-1
                elif nextStep==1:
                        j = j+1
                        i = i+1
                elif nextStep==2:
                        j = j-1
                nextStep = nextStep +1
                if nextStep==3:
                        nextStep=0
                        
                if f1 or f2:
                        continue
                
                while m<n:
                        c = nums[m]
                        d = nums[n]
                        f3 = c!=nums[m-1] if m>i+1 else True
                        f4 = d!=nums[n+1] if n<j-1 else True
                        f = f3 and f4
                        s = a+b+c+d
                        print(a,c,d,b,s==target,i,j)
                        if s==target and f:
                                res.append([a,c,d,b])
                                m = m+1
                                n = n-1
                        elif s>target:
                                n = n-1
                        elif s<target:
                                m = m+1
                        else:
                                m = m+1
                                n = n-1
        return  res

a = fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5],0)  #-2 -1 0 0 1 2
print(a)
    
