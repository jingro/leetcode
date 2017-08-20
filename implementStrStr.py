class Solution(object):
    def strStr(self, haystack, needle):
        M, N = len(haystack), len(needle)
        i = j = 0
        while i < M:
            while j < N:
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    break
            if j == N:
                return i
            i += 1
