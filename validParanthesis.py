class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sta = []
        a = ['(', '[', '{']
        b = [')', ']', '}']
        for i in s:
            if i in a:
                sta.append(i)
            else:
                t = b.index(i)
                if sta and sta[-1] == a[t]:
                    sta.pop()
                else:
                    return False
        return len(sta) == 0
