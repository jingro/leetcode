class Solution(object):
    def longestPalindrome(self, s):
        size = len(s)
        if size <= 1:
            return s
        maxSize = 1
        res = s[0]
        i = j = k = 0
        while i < size:
            j = k = i
            if i > 0 and s[i] == s[i - 1]:
                j = i - 1
                k = i
            elif i < size - 1 and s[i] == s[i + 1]:
                j = i
                k = i + 1
            while j >= 0 and k < size and s[j] == s[k]:
                j -= 1
                k += 1
            t = k - j - 1
            if t > maxSize:
                maxSize = t
                res = s[j + 1:k]

            j = i - 1
            k = i + 1
            while j >= 0 and k < size and s[j] == s[k]:
                j -= 1
                k += 1
            t = k - j - 1
            if t > maxSize:
                maxSize = t
                res = s[j + 1:k]
            i += 1
        return res
