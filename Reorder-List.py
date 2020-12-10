class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if not head: 
            return
        
        prev = None
        head2 = head
        h = head
        length = 0
        while h.next:
            h = h.next
            length += 1
        for i in range((length + 2) // 2):
            prev = head2
            head2 = head2.next
            
        prev.next = None
        
        h2 = None
        while head2:
            h2 = ListNode(head2.val, h2)
            head2 = head2.next
            
        h1 = head
        
        while h1 and h2:
            h1Next = h1.next 
            h1.next = h2 
            h2Next = h2.next 
            h2.next = h1Next 
            h1 = h1Next
            h2 = h2Next
        
        return head
