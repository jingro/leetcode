class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t = [0 for i in range(m + n)]
        i = j = k = 0
        while i < m or j < n:
            if i == m:
                t[k] = nums2[j]
                j += 1
            elif j == n:
                t[k] = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                t[k] = nums1[i]
                i += 1
            else:
                t[k] = nums2[j]
                j += 1
            k += 1
        nums1[:m + n] = t



