class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        head = headA
        while head:
            head.val *= -1
            head = head.next
        head = headB
        while head and head.val > 0:
            head = head .next
        h = head
        head = headA
        while head and head.val < 0:
            head.val *= -1
            head = head.next
        return h
