# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = head
        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)
e = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = e
deleteDuplicates(a)
