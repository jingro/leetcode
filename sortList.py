# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p, q = head, head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
        q = p.next
        p.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(q)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        res = t = ListNode(-1)
        while l1 or l2:
            if not l1:
                t.next = l2
                l2 = l2.next
            elif not l2:
                t.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        return res.next
