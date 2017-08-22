class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        a = []
        for (key, val) in d.items():
            a.append((key, val))
        self.aux(a, [], res, len(nums))
        return res

    def aux(self, a, t, res, size):
        if len(t) == size:
            res.append(t[:])
            return
        for i in a:
            cnt = 0
            for j in t:
                if i[0] == j:
                    cnt += 1
            if i[1] > cnt:
                t.append(i[0])
                self.aux(a, t, res, size)
                t.pop()
