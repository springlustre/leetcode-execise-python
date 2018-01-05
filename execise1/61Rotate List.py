class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
def rotateRight(head,k):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not head:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length+=1
        tail.next = head

        n = k % length
        for i in range(length-n):
            tail = tail.next
        res = tail.next
        tail.next = None
        # while head:
        #     print(head.val)
        #     head = head.next
                
        return res

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
a = rotateRight(n1,2)
print(a)
    
