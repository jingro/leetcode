# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cnt = 0
        p = head
        while p:
            p = p.next
            cnt += 1
        i, j = 1, cnt
        return self.aux(head, i, j)[1]

    def aux(self, head, lo, hi):
        if lo > hi:
            return head, None
        mid = (lo + hi) / 2
        head, l = self.aux(head, lo, mid - 1)
        t = TreeNode(head.val)
        t.left = l
        head = head.next
        head, t.right = self.aux(head, mid + 1, hi)
        return head, t
