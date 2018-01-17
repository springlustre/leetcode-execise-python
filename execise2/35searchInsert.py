def searchInsert(nums,target):
        
        high = len(nums)-1
        low=0
        while low<high:
                print(low,high)
                mid = (low+high)//2
                m = nums[mid]
                if target == m:
                        return mid
                elif target>m:
                        low = mid+1
                else:
                        high = mid
        if nums[low]>=target:
                return low
        else:
                return low+1

a = searchInsert([1,3,5,6],0)
print(a)
    
