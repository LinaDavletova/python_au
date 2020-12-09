class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head2 = head
        num = 0
        while head2:
            head2 = head2.next
            num += 1
        for i in range(num/2):
            head = head.next
        rec = ListNode(head.val)
        return head
