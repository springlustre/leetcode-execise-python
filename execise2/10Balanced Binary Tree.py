def isBalanced(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def myBalance(root):
                if not root:
                        return (True,0)
                else:
                        res1= myBalance(root.left)
                        res2 = myBalance(root.right)
                        b1 = res1[0]
                        l = res[1]
                        b2 = res2[0]
                        r = res2[1]
                        if b1 and b2:
                                if l>r:
                                        if l-r<=1:
                                                return (l+1,True)
                                        else:
                                                return (l+1,False)
                                else:
                                        if r-l<=1:
                                                return (r+1,True)
                                        else:
                                                return (r+1,False)
                        else:
                                return False
        res = myBalance(root)
        return res[0]