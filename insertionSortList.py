# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        res.next = head
        cur = head
        while cur and cur.next:
            key = cur.next.val
            if cur.val <= key:
                cur = cur.next
                continue
            if prev.next.val > key:
                prev = res
            while prev.next != cur.next and prev.next.val <= key:
                prev = prev.next
            if prev.next.val > key:
                t = cur.next
                cur.next = cur.next.next
                t.next = prev.next
                prev.next = t
            else:
                cur = cur.next
        return res.next
