def connect(self, root):
        level = [root] if root else []
        while level:
                temp = []
                pre = None
                for x in level:
                        if pre:
                                pre.next = x
                        pre = x
                        if x.left:
                                temp.append(x.left)
                        if x.right:
                                temp.append(x.right)
                pre.next = None
                level = temp