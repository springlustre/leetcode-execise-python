def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #         return 0
        # res = 0
        # level = [root]
        # while level:
        #         nextLevel = []
        #         for x in level:
        #                 if x.left:
        #                         nextLevel.append(x.left)
        #                 if x.right:
        #                         nextLevel.append(x.right)
        #         res+=1
        #         level = nextLevel
        # return res

        def myDeep(p):
                if not p:
                        return 0
                elif not p.left and not p.right:
                        return 1
                else:
                        return max(myDeep(p.left,p.right))+1