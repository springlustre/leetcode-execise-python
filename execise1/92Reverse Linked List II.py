# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    temp = ListNode(0)
    temp.next = head
    cur = temp
    for i in range(1,m):
        cur = cur.next
        head = head.next
    for i in range(m,n):
        t = ListNode(head.next.val)
        t.next = cur.next
        cur.next = t
        head.next = head.next.next

    while temp:
        print(temp.val)
        temp = temp.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

reverseBetween(a,1,1)