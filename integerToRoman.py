class Solution(object):
    def intToRoman(self, num):
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i, res = 0, []
        while num:
            cnt = num / a[i]
            num %= a[i]
            for j in range(cnt):
                res.append(b[i])
            i += 1
        return ''.join(res)
