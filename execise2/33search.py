def search(nums,target):
        
        high = len(nums)-1
        low=0
        while low<=high:
                   #print(low,high)
                   mid = (low+high)//2
                   m = nums[mid]
                   if target == m:
                           return mid
                   elif m < nums[high]:
                           if target>m and target<=nums[high]:
                                   low = mid+1
                           else:
                                   high = mid
                   else:#左边有序
                           if target<m and target>=nums[low]:
                                   high = mid
                           else:
                                   low = mid+1
  
        return  -1

a = search([1,3],3)
print(a)
    
