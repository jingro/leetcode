# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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
