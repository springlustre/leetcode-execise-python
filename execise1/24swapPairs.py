def swapPairs(head):
        """"
        :type head: ListNode
        :rtype: ListNode
        """
        temp = cursor =ListNode(0)
        head1 = ListNode(0)
        head1.next = head        
        while head1.next:
            if head1.next.next:
                t = ListNode(head1.next.val)
                head1 = head1.next.next
                t2 = ListNode(head1.val)
                cursor.next = t2
                cursor = cursor.next
                cursor.next = t
                cursor = cursor.next
            else:
                head1 = head1.next
                t2 = ListNode(head1.val)
                cursor.next = t2
                cursor = cursor.next
                
                
        return temp.next

a = swapPairs([1,2,3,4,5])
print(a)
    
