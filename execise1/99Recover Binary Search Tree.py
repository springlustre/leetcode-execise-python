class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    # stack = []
    # temp1 = None
    # temp2 = None
    # time = 0
    # res = []
    # i = 0
    # while root or stack:
    #     while root:
    #         stack.append(root)
    #         root = root.left
    #     root = stack.pop()
    #     if not res or (res[-1].val < root.val):
    #         res.append(root)
    #         root = root.right
    #     else:
    #         time+=1
    #         if time==1:
    #             temp1 = res[-1]
    #             i = len(res)
    #         elif time==2:
    #             temp2 = root
    #         else:
    #             break
    #         res.append(root)
    #         root = root.right
    #
    # if not temp2:
    #     temp2 = res[i]
    # v = temp1.val
    # temp1.val = temp2.val
    # temp2.val = v

    t1 = None
    t2 = None
    cur = root
    pre = None
    last = None
    time = 0
    while cur:
        if not cur.left:
            if not last or cur.val > last.val:
                last = cur
                cur = cur.right
            else:
                time+=1
                if time==1:
                    t1 = last
                    t2 = cur
                elif time==2:
                    t2 = cur
                last = cur
                cur = cur.right
        else: #
            pre = cur.left
            while pre.right and pre.right!=cur:
                pre = pre.right
            if not pre.right:
                pre.right = cur
                cur = cur.left
            else: # has linked cur
                if not last or cur.val > last.val:
                    last = cur
                    cur = cur.right
                else:
                    time+=1
                    if time==1:
                        t1 = last
                        t2 = cur
                    elif time==2:
                        t2 = cur
                    last = cur
                    cur = cur.right

     v = t1.val
    t1.val = t2.val
    t2.val = v



    #    a
    # b    d
    #   c e
a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(4)
a.left = b
b.right = c
a.right = d
d.left = e

res = recoverTree(a)