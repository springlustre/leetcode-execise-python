def combinationSum(candidates,target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def cal(arr,target,index,path,res):
                if target<0:
                        return
                elif target==0:
                        res.append(path)
                        return
                for i in range(index,len(arr)):
                        cal(arr,target-arr[i],i,path+[arr[i]],res)
        
        cal(candidates,target,0,[],res)  

        return  res

a = combinationSum([1],1)
print(a)
    
