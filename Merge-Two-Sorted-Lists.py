class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            prev = l1.val
            l3 = ListNode(l1.val)
            l1 = l1.next
        else:
            prev = l2.val
            l3 = ListNode(l2.val)  
            l2 = l2.next
        while (l1) and (l2):
            if l1.val < l2.val:
                l3 = ListNode(l1.val, l3)
                l1 = l1.next
            else:
                l3 = ListNode(l2.val, l3)
                l2 = l2.next
        while l1:
            l3 = ListNode(l1.val, l3)
            l1 = l1.next
        while l2:
            l3 = ListNode(l2.val, l3)
            l2 = l2.next
        if l3 is None:
            return l3
        rec = ListNode(l3.val)
        l3 = l3.next
        while l3:
            rec = ListNode(l3.val, rec)
            l3 = l3.next
        return rec
