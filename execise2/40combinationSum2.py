def combinationSum2(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        length = len(candidates)
        def cal(arr,i,tar,sub,res):
                if tar < 0:
                        return
                elif tar==0:
                        res.append(sub)
                        return
                else:
                        for k in range(i,length):
                                if k>i and arr[k]==arr[k-1]:
                                        continue
                                s = sub+[arr[k]]
                                cal(arr,k+1,tar-arr[k],s,res)
        cal(candidates,0,target,[],res)
        return  res

a = combinationSum2([10, 1, 2, 7, 6, 1, 5],8)
print(a)
    
