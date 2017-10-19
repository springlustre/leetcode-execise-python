def removeNthFromEnd(head,n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = p2 = head
        for _ in range(n):
            p1 = p1.next
        if not p1:#p1为空则n为length-1
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head

a = removeNthFromEnd([1,2,3,4,5],2)
print(a)
    
