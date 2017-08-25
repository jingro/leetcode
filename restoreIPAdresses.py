class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.aux(s, [], res, 0)
        return res

    def aux(self, s, ip, res, beg):
        if len(ip) == 4 and beg == len(s):
            t = '.'.join(ip)
            res.append(t)
            return
        if len(s) - beg > 3 * (4 - len(ip)) or len(s) - beg < 4 - len(ip):
            return
        num = 0
        for i in range(beg, beg + 3):
            if i == len(s):
                return
            num = num * 10 + int(s[i])
            if num > 255:
                continue
            ip.append(s[beg:i + 1])
            self.aux(s, ip, res, i + 1)
            ip.pop()
            if not num:  # after pop, should not go on with prefix 0
                break
