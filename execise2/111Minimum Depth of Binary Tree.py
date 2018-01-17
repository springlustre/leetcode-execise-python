def minDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def myMin(root):
                if not root.left and not root.right:
                        return 1
                if not root.left:
                        return 1+myMin(root.right)
                elif not root.right:
                        return 1+myMin(root.left)
                else:
                        return 1+min(myMin(root.left),myMin(root.right))
        if not root:
                return 0
        return myMin(root)