# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head:
        return head
    cur = ListNode(head.val-1)
    cur.next = head
    last = cur
    res = last
    while cur and cur.next:
        print(cur.val,last.val)
        if cur.next.val < x:
            if cur.val < x:
                cur = cur.next
                last = last.next
            else:
                temp = ListNode(cur.next.val)
                cur.next = cur.next.next
                # cur = cur.next
                temp.next = last.next
                last.next = temp
                last = last.next
        else:
            cur = cur.next

    while res:
        print(res.val)
        res = res.next

a = ListNode(3)
b = ListNode(1)
c = ListNode(2)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
# c.next = d
# d.next = e
# e.next = f
partition(a,3)
