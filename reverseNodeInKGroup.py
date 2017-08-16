# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        cnt /= k
        res = ListNode(-1)
        res.next = head
        prev, cur = res, res.next
        for i in range(cnt):
            for j in range(k - 1):
                t = cur.next
                cur.next = t.next
                t.next = prev.next
                prev.next = t
            prev = cur
            cur = prev.next
        return res.next
