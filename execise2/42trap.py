def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
                return 0
        
        res = 0
        a = 0
        b = len(height)-1
        leftMax = height[a]
        rightMax = height[b]
        while a<b:
                leftMax = height[a] if height[a]>leftMax else leftMax
                rightMax = height[b] if height[b]>rightMax else rightMax
                if leftMax < rightMax:
                        res += leftMax-height[a]
                        a +=1
                else:
                        res += rightMax - height[b]
                        b-=1
        return res


a = trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(a)
    
