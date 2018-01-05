def getPermutation(n,k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """     
        
##        def cal(nums):
##                if len(nums)==0:
##                        return [""]
##                if len(nums)==1:
##                        return [str(nums[0])]
##                else:
##                        res = []
##                        for x in nums:
##                                param = nums[:]
##                                param.remove(x)
##                                for r in cal(param):
##                                        t = str(x)+r
##                                        res.append(t)
##                        return res
##        res = []
##        nums = [i for i in range(1,n+1)]
##        for x in range(1,n+1):
##                param = nums[:]
##                param.remove(x)
##                for r in cal(param):
##                        t = str(x)+r
##                        res.append(t)
##        t = res[k-1]
##        return  t
##                4*3*2 = 24
##        1234       
##        1243      
##        1324       3  n/3!
##        1342

        def cal(n):
                res = 1
                for i in range(1,n+1):
                        res=res*i
                return res
        
        i = n
        nums = [i for i in range(1,n+1)]
        res = ""
        remain = k-1
        while i>1:
##                print("i=",i)
                temp = cal(i-1)
##                print("temp",temp)
                m = remain//temp
                remain -= temp*m
##                print("remain",remain)
##                print("m=",m)
                cur = nums[m]
                res+=str(cur)
##                print("res",res)
                nums.remove(cur)
                i-=1
        res+=str(nums[0])
        return res

        

a = getPermutation(4,5)
print(a)
    
