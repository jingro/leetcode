# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        res = t = RandomListNode(-1)
        p = head
        d = {}
        while p:
            t.next = RandomListNode(p.label)
            d[p] = t.next
            p = p.next
            t = t.next
        p, t = head, res.next
        while p:
            if p.random:
                t.random = d[p.random]
            p = p.next
            t = t.next
        return res.next
