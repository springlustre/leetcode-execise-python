def searchRange(nums,target):
        
        res = 0
        high = len(nums)-1
        high2 = high
        low = 0
        low2 = 0
        while low<high:
                   mid = (low+high)//2
                   m = nums[mid]
                   if target>m:
                           low = mid+1
                   else:
                           high = mid
        index1 = low
        while low2 < high2:
                mid2 = (low2+high2)//2+1
                m = nums[mid2]
                if target < m:
                        high2 = mid2-1
                else:
                        low2 = mid2
                #print(low2,high2)
        index2 = high2
        if len(nums)==0 or nums[index1]!=target:
                return [-1,-1]
        else:
                return [index1,index2]

a = searchRange([1,2,3,3,3,3,4,5],3)
print(a)
    
