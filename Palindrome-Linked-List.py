class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        head2 = head
        rec = ListNode(head2.val)
        head2 = head2.next
        while head2:
            rec = ListNode(head2.val, rec)
            head2 = head2.next
        while (head) and (head.val == rec.val):
            head = head.next
            rec = rec.next

        if head == rec:
            return True
        return False
