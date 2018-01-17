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
        if not head or not head.next:
            return head
        last = ListNode(0)
        last.next = head
        res = last
        repeat = False
        while head.next:
            if head.val == head.next.val:
                repeat = True
                head = head.next
            else:
                head = head.next
                if not repeat:
                    last = last.next
                last.next = head
                repeat = False
        if repeat:
            last.next = None

        while res:
            print(res.val)
            res = res.next
        return head

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
