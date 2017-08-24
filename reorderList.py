# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        prev = p = q = head
        while q and q.next:
            prev = p
            p = p.next
            q = q.next.next
        prev.next = None
        head2 = ListNode(-1)
        head2.next = p
        while p.next:
            t = p.next
            p.next = t.next
            t.next = head2.next
            head2.next = t
        t = ListNode(-1)
        p, q = head, head2.next
        while p and q:
            t.next = p
            p = p.next
            t = t.next
            t.next = q
            q = q.next
            t = t.next
        if q:
            t.next = q
