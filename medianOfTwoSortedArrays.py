class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        if size % 2:
            return self.select(nums1, nums2, size / 2 + 1)
        else:
            return (self.select(nums1, nums2, size / 2)
                    + self.select(nums1, nums2, size / 2 + 1)) / 2.0

    def select(self, nums1, nums2, d):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.select(nums2, nums1, d)
        if not m:
            return nums2[d - 1]
        if d == 1:
            return min(nums1[0], nums2[0])

        i = min(m, d / 2)
        j = d - i
        if nums1[i - 1] < nums2[j - 1]:
            return self.select(nums1[i:], nums2, d - i)
        elif nums1[i - 1] > nums2[j - 1]:
            return self.select(nums1, nums2[j:], d - j)
        else:
            return nums1[i - 1]
