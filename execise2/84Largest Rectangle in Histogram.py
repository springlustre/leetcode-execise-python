
def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if not heights:
        return 0

    # stack = []
    # heights.append(-1)
    # length = len(heights)
    # res = 0
    # i = 0
    # while i < length:
    #     if len(stack)==0 or heights[stack[-1]] <=heights[i]:
    #         stack.append(i)
    #         i+=1
    #     else:
    #         last = stack.pop()
    #         s = 0
    #         if len(stack)==0:
    #             s = i * heights[last]
    #         else:
    #             s = heights[last] * (i - stack[-1]-1)
    #         print(i,s)
    #         if res<s:
    #             res = s
    # return res






a = largestRectangleArea([2,1,5,6,5,3])
print(a)