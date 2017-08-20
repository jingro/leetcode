class Solution(object):
    def longestCommonPrefix(self, strs):
        # size = min([len(i) for i in strs])
        size = len(strs[0])
        for i in range(size):
            t = strs[0][:i + 1]
            for s in strs:
                if s[:i + 1] != t:
                    return s[:i]
        return strs[0]
