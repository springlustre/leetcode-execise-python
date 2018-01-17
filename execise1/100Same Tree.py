def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    def mySame(t1,t2):
        if not t1 and not t2:
            return True
        if t1 and t2:
            return t1.val==t2.val and mySame(t1.left,t2.left) and mySame(t1.right,t2.right)
        else:
            return False
    return mySame(p,q)
