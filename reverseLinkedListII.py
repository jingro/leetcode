# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(-1)
        res.next = head
        prev = res
        for i in range(m - 1):
            prev = prev.next
        head2 = prev
        prev = head2.next
        cur = prev.next
        for i in range(m, n):
            prev.next = cur.next
            cur.next = head2.next
            head2.next = cur
            cur = prev.next
        return res.next
