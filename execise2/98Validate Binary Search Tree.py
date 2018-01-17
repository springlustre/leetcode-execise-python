class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # def maxChild(root):
    #     if not root.left and not root.right:
    #         return root.val
    #     elif not root.left:
    #         return max(root.val, maxChild(root.right))
    #     elif not root.right:
    #         return max(root.val, maxChild(root.left))
    #     else:
    #         l = maxChild(root.left)
    #         r = maxChild(root.right)
    #         return max(root.val, max(l,r))
    # def minChild(root):
    #     if not root.left and not root.right:
    #         return root.val
    #     elif not root.left:
    #         return min(root.val, minChild(root.right))
    #     elif not root.right:
    #         return min(root.val, minChild(root.left))
    #     else:
    #         l = minChild(root.left)
    #         r = minChild(root.right)
    #         return min(root.val, min(l,r))
    #
    # def myValid(root):
    #     if not root:
    #         return True
    #     l = root.left
    #     r = root.right
    #     if  l and  r:
    #         print(maxChild(l),maxChild(r))
    #         res = root.val >maxChild(l) and root.val<minChild(r)
    #         return myValid(l) and myValid(r) and res
    #     elif l:
    #         res = root.val >maxChild(l)
    #         return myValid(l)  and res
    #     elif r:
    #         res = root.val<minChild(r)
    #         return myValid(r) and res
    #     else:
    #         return True

    # return myValid(root)

    stack = []
    res = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not res or (res and root.val>res[-1]):
            res.append(root.val)
            root = root.right
        else:
            return False
    return True



    #    a
    # b    d
    #   c e
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(4)
a.left = b
b.right = c
a.right = d
d.left = e

res = isValidBST(a)
print(res)