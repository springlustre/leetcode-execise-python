def flatten(root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
                if not cur.left:
                        cur = cur.right
                        continue
                left = cur.left
                temp = left
                while temp.right:
                        temp = temp.right
                temp.right = cur.right
                cur.right = left
                cur.left = None
                cur = left