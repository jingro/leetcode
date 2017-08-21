class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sta = []
        last, res = -1, 0
        size = len(s)
        for i in range(size):
            if s[i] == '(':
                sta.append(i)
            else:
                if not sta:
                    last = i
                else:
                    sta.pop()
                    if not sta:
                        res = max(res, i - last)
                    else:
                        res = max(res, i - sta[-1])
        return res
