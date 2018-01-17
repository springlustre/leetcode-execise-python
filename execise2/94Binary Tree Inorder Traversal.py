# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        t2 = stack.pop()
        res.append(t2.val)
        root = t2.right
    print(res)
    return res

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
a = inorderTraversal(a)
print(a)
