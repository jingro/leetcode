class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        sign = False
        digit = False
        dot = False
        eflag = False
        i, size = 0, len(s)
        while i < size:
            if not sign and (s[i] == '+' or s[i] == '-'):
                i += 1
                sign = True
            elif s[i].isdigit():
                i += 1
                digit = True
                sign = True
            elif not dot and s[i] == '.':
                i += 1
                dot = True
                sign = True
            elif digit and not eflag and (s[i] == 'e' or s[i] == 'E'):
                i += 1
                eflag = True
                dot = True
                sign = False
                digit = False
            else:
                return False
        if digit:
            return True
        return False
