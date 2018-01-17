# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    res = []
    def myGenerate(start,end):
        if start>end:
            return [None]
        if start==end:
            return [TreeNode(start)]
        res = []
        for i in range(start,end+1):
            left = myGenerate(start,i-1)
            right = myGenerate(i+1,end)
            for l in left:
                for r in right:
                    p = TreeNode(i)
                    p.left = l
                    p.right = r
                    res.append(p)
        return res

    return myGenerate(1,n)





#     1
# 2      4
#   3  5
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
b.right = c
a.right = d
d.left = e
a = generateTrees(3)
print(a)