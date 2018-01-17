def isSymmetric(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def mySame(p,q):
                if not p and not q:
                        return True
                elif p and q:
                        return p.val==q.val and mySame(p.left,q.left) and mySame(p.right,q.right)
                else:
                        return False
        if not root:
                return True
        mySame(root.left,root.right)
