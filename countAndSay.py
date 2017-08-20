class Solution(object):
    def countAndSay(self, n):
        res = ['1']
        for i in range(1, n):
            j, size = 0, len(res)
            t, res = res, []
            while j < size:
                cnt = 1
                while j < size - 1 and t[j] == t[j + 1]:
                    cnt += 1
                    j += 1
                res.append(str(cnt))
                res.append(t[j])
                j += 1
        return ''.join(res)

