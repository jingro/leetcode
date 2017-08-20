class Solution(object):
    def addBinary(self, a, b):
        M, N = len(a), len(b)
        z = 0
        i, j = M - 1, N - 1
        res = []
        while i >= 0 or j >= 0 or z:
            x = ord(a[i]) - ord('0') if i >= 0 else 0
            y = ord(b[j]) - ord('0') if j >= 0 else 0
            sum = x + y + z
            z = sum / 2
            t = sum % 2
            res.append(chr(t + ord('0')))
            i -= 1
            j -= 1
        res.reverse()
        return ''.join(res)
