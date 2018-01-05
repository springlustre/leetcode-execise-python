def search(nums, target):

    i,j = 0,len(nums)-1
    while i<=j:
        m = (i+j)//2
        left = nums[i]
        right = nums[j]
        middle = nums[m]
        print(left,middle,right,i,j,m)
        if middle==target:
            return True
        if right < middle:
            if left <= target <middle:
                j = m-1
            else:
                i = m+1
        elif middle < right:
            if middle<target<=right:
                i = m+1
            else:
                j = m-1
        else:
            j-=1
    return target==nums[j]


a = search([2,2,2,0,2,2],0)
print(a)
    
