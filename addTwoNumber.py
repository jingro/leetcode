# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = head = ListNode(-1)
        c = 0
        while l1 or l2 or c:
            a, b = l1.val if l1 else 0, l2.val if l2 else 0
            sum = a + b + c
            x = sum % 10
            c = sum / 10
            head.next = ListNode(x)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next
