def zigzagLevelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
                return res
        level = [root]
        order = True
        while level:
                t = []
                next = []
                if order:
                        for x in level:
                                t.append(x.val)
                                if x.left:
                                        next.append(x.left)
                                if x.right:
                                        next.append(x.right)
                        res.append(t)
                        level = next
                        order = False
                else:
                        for x in level:
                                t.insert(0,x.val)
                                if x.left:
                                        next.append(x.left)
                                if x.right:
                                        next.append(x.right)
                        res.append(t)
                        level = next
                        order = True
        return res
