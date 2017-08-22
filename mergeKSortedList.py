# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        size = len(lists)
        if not size:
            return
        while len(lists) != 1:
            j = 0
            size = len(lists)
            while j < size / 2:
                lists[j] = self.aux(lists[j], lists[size - j - 1])
                lists.pop(size - j - 1)
                j += 1
        return lists[0]

    def aux(self, l1, l2):
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
