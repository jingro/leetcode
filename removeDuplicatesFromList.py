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
        if not head:
            return
        i, j = head.next, head
        while i:
            if i.val != j.val:
                j.next = i
                j = j.next
            i = i.next
        j.next = None
        return head
