def connect(root):
        cur = root
        while cur:
                t = cur
                p = None
                f = True
                while t:
                        left = t.left
                        right = t.right
                        if left:
                                if p:
                                        p.next = left
                                p = left
                                if f:
                                        cur = left
                                        f = False
                        if right:
                                if p:
                                        p.next = right
                                p = right
                                if f:
                                        cur = right
                                        f = False
                        t = t.next
                if f:
                        cur = None

