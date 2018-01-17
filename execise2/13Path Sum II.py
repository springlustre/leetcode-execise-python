def pathSum(root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def myFunc(root,sum):
                if not root.left and not root.right:
                        s = sum - root.val
                        if s==0:
                                return [[root.val]]
                        else:
                                return []
                v = root.val
                s = sum - v
                if not root.left:
                        r = myFunc(root.right,s)
                        temp = []
                        for x in r:
                                x.insert(0,v)
                                temp.append(x)
                        return temp
                elif not root.right:
                        r = myFunc(root.left,s)
                        temp = []
                        for x in r:
                                x.insert(0,v)
                                temp.append(x)
                        return temp
                else:
                        r1 = myFunc(root.left,s)
                        r2 = myFunc(root.right,s)
                        temp = []
                        r1.extend(r2)
                        for x in r1:
                                x.insert(0,v)
                                # print("x",x)
                                temp.append(x)
                        # print("temp",temp)
                        return temp

        if not root:
                return []
        res = []
        t = myFunc(root,sum)
        # for x in t:
        #     x.reverse()
        #     res.append(x)
        return t