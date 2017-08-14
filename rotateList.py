# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cnt = 1
        p = head
        while p.next:
            p = p.next
            cnt += 1
        k %= cnt
        if not k:
            return head
        k = cnt - k
        q = head
        for i in range(k - 1):
            q = q.next
        res = q.next
        q.next = None
        p.next = head
        return res
