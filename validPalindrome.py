class Solution(object):
    def isPalindrome(self, s):
        size = len(s)
        lo, hi = 0, size - 1
        s = s.lower()
        while lo < hi:
            while not s[lo].isalnum():
                lo += 1
            while not s[hi].isalnum():
                hi -= 1
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                return False
        return True
