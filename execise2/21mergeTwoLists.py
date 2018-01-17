def mergeTwoLists(l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = head = ListNode(0)
        if not l1:
                return l2
        if not l2:
                return l1
        while l1 and l2:
                if l1.val < l2.val:
                        head.next = l1
                        l1 = l1.next
                else:
                        head.next = l2
                        l2 = l2.next
                head = head.next

        if l1:
                head.next = l1
        else:
                head.next = l2
                
        return temp.next

a = mergeTwoLists([1,2,3,4,5],[1,2,3])
print(a)
    
