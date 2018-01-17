def buildTree(preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def myBuild(p1,p2,i1,i2):
                if p1>p2 or i1>i2:
                        return None
                else:
                        node = preorder[p1]
                        root = TreeNode(node)
                        i = inorder.index(node)
                        left = myBuild(p1+1,i-i1+p1,i1,i-1)
                        right = myBuild(i+1-i2+p2,p2,i+1,i2)
                        root.left = left
                        root.right = right
                        return root
        length = len(preorder)
        return myBuild(0,length-1,0,length-1)

        # def myBuild(pre,inorder):
        #         if not pre:
        #                 return None
        #         node = pre[0]
        #         root = TreeNode(node)
        #         i = inorder.index(node)
        #         left = myBuild(pre[1:i+1],inorder[:i])
        #         right = myBuild(pre[i+1:],inorder[i+1:])
        #         root.left = left
        #         root.right = right
        #         return root
        # return myBuild(preorder,inorder)

