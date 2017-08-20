class Solution(object):
    def myAtoi(self, str):
        INT_MAX = 2147483647
        str = str.strip()
        i, size = 0, len(str)
        sign, res = 1, 0
        if str and str[0] == '-':
            sign = -1
            i += 1
        elif str and str[0] == '+':
            i += 1
        while i < size:
            t = str[i]
            if not t.isdigit():  # important
                break
            t = ord(t) - ord('0')
            if res > INT_MAX / 10 or (res == INT_MAX / 10 and t > INT_MAX % 10):
                return INT_MAX if sign == 1 else -INT_MAX - 1  # judge before new res calculated
            res = res * 10 + t
            i += 1
        return res * sign
