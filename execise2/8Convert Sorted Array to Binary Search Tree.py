def sortedArrayToBST(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        1  2  3  4   5  6   7
        4
    2        6
1      3  5    7

        def myConv(start,end):
                if start>end:
                        return None
                k = (start+end+1) // 2
                root = TreeNode(nums[k])
                left = myConv(start,k-1)
                right = myConv(k+1,end)
                root.left = left
                root.right = right
                return root
        return myConv(0,len(nums)-1)

