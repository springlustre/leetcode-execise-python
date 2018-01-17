def permute(nums):
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
                                t = arr[:i]+arr[i+1:]
                                for l in gen(t):
                                        #print("l",l)
                                        tmp.append([arr[i]]+l)
                        return tmp

        res = gen(nums)
        return res

a = permute([])
print(a)
    
