class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def MergeSort(head):
            num = 0
            h = head
            while h:
                num += 1
                h = h.next
            if num < 2:
                return head
            if num > 2:
                return Merge(MergeSort(firstPart(head, num)), MergeSort(lastPart(head, num)))
            if head and head.next and head.val > head.next.val:
                a = ListNode(head.val, None)
                b = ListNode(head.next.val, None)
                b.next = a
                return (b)
            return head
        def firstPart(head, num):
            for i in range(num / 2):
                head = head.next
            return head
        def lastPart(head, num): 
            h = None
            for i in range(num / 2):
                h = ListNode(head.val, h)
                head = head.next
            return h
        def Merge(l1, l2):
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
        return MergeSort(head)
