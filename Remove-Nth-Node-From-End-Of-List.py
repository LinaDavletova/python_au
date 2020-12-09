class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        rec = ListNode(head.val)
        head = head.next
        head2 = head
        num = 0
        while head2:
            head2 = head2.next
            num += 1
        while head:
            rec = ListNode(head.val, rec)
            head = head.next
        if num == 0:
            return head
        ans = ListNode(rec.val)
        rec = rec.next
        if n == 1:
            ans = ListNode(rec.val)
            rec = rec.next
            num -= 1
        for i in range(num):
            if i != n-2:
                ans = ListNode(rec.val, ans)
            rec = rec.next
        return ans
