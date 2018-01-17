def hasPathSum(root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def myFunc(root,sum):
                if not root:
                        return True if sum==0 else False
                s = sum - root.val
                if not root.left:
                        return myFunc(root.right,s)
                elif not root.right:
                        return myFunc(root.left,s)
                else:
                        return myFunc(root.left,s) or myFunc(root.right,s)
        if not root:
                return False
        return myFunc(root,sum)