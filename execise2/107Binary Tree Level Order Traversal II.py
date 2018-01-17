def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return []
    level = [root]
    while level:
        t = []
        tempLevel = []
        for x in level:
            t.append(x.val)
            if x.left:
                tempLevel.append(x.left)
            if x.right:
                tempLevel.append(x.right)
        res.insert(0,t)
        level = tempLevel
    return res
