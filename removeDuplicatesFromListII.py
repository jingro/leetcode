# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = t = ListNode(-1)
        p, q = head, head.next
        while q:
            if p.val != q.val:
                t.next = p
                t = t.next
            else:
                while p.next and p.val == p.next.val:
                    p = p.next
            p = p.next
            q = p.next if p else None
        t.next = p
        return res.next
