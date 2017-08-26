class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = cnt = 0
        for i in range(len(s)):
            if s[i] in d:
                cnt = max(cnt, i - l)
                l = max(l, d[s[i]] + 1)
            d[s[i]] = i
        return max(cnt, len(s) - l)
