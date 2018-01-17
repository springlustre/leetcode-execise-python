def levelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        flag = True
        res = []
        level = [root]
        while level:
                t = []
                t2 = []
                for x in level:
                        if x:
                                t.append(x.val)
                                t2.append(x.left)
                                t2.append(x.right)
                if t:
                        res.append(t)
                level = t2
        return res
