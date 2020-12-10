# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
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
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
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
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
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
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
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
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
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
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    p1 = head
    p2 = head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            p1 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p2
    return None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return None
    p1 = head
    p2 = head
    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return 1
    return None
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
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
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
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
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
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
```

