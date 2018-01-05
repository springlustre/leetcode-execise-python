# Definition for singly-linked list.
def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    # if not matrix or not matrix[0]:
    #     return 0
    # n = len(matrix[0])
    # height = [0] * (n + 1)
    # ans = 0
    # for row in matrix:
    #     for i in range(n):
    #         height[i] = height[i] + 1 if row[i] == '1' else 0
    #     stack = [-1]
    #     print(height)
    #     for i in range(n + 1):
    #         while height[i] < height[stack[-1]]:
    #             h = height[stack.pop()]
    #             w = i - 1 - stack[-1]
    #             ans = max(ans, h * w)
    #         stack.append(i)
    # return ans

    if not matrix or not matrix[0]:
        return 0
    col = len(matrix[0])
    res = 0
    length = col+1
    height = [0 for _ in range(length)]
    for r in matrix:
        for i in range(col):
            height[i] = height[i]+1 if r[i]=="1" else 0
        stack = []
        i = 0
        while i < length:
            h = height[i]
            if len(stack)==0 or height[stack[-1]]<=h:
                stack.append(i)
                i+=1
            else:
                t = stack.pop()
                s = 0
                if len(stack)==0:
                    s = i * height[t]
                else:
                    s = height[t]*(i-stack[-1]-1)
                if res<s:
                    res = s

    return res



a = maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
])

print(a)