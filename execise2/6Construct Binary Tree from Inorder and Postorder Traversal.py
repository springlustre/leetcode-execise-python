def buildTree(inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        m = {}
        i=0
        for k in inorder:
                m[k] = i
                i+=1

        def myBuild(iStart,iEnd,pStart,pEnd):
                if pStart>pEnd:
                        return None
                node = postorder[pEnd]
                i = m[node]
                root = TreeNode(node)
                left = myBuild(iStart,i-1, pStart, i-1-iStart+pStart)
                right = myBuild(i+1,iEnd, i+1-iEnd+pEnd-1, pEnd-1)
                root.left = left
                root.right = right
                return root
        length = len(inorder)
        return myBuild(0,length-1,0,length-1)
