# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = b = head
        while b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                c = head
                while a != c:
                    c = c.next
                    a = a.next
                return c
