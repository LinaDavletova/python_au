class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        rec = ListNode(head.val)
        head = head.next
        while head:
            rec = ListNode(head.val, rec)
            head = head.next
        return rec
