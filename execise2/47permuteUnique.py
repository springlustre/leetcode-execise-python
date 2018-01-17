def permuteUnique(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def gen(arr):
                if len(arr)==1:
                        return [arr]
                else:
                        #print(arr)
                        tmp = []
                        for i in range(len(arr)):
                                if not (i>0 and arr[i]==arr[i-1]):
                                        t = arr[:i]+arr[i+1:]
                                        for l in gen(t):
                                                #print("l",l)
                                                tmp.append([arr[i]]+l)
                        return tmp

        res = gen(nums)
        return res

a = permuteUnique([1,1,2])
print(a)
    
