def sortedListToBST(head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def mySort(head,tail):
                slow = head
                fast = head
                if head==tail:
                        return None
                while fast!=tail and fast.next!=tail:
                        slow = slow.next
                        fast = fast.next.next
                # print(slow.val,fast.val)
                root = TreeNode(slow.val)
                left = mySort(head,slow)
                right = mySort(slow.next,tail)
                root.left = left
                root.right = right
                return root
        return mySort(head,None)