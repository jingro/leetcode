class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.aux(candidates, target, [], res, 0)
        return res

    def aux(self, candidates, gap, path, res, beg):
        if not gap:
            res.append(path[:])
            return
        used = -1
        for i in range(beg, len(candidates)):
            if gap < candidates[i]:
                return
            if used == candidates[i]:
                continue
            path.append(candidates[i])
            used = candidates[i]
            self.aux(candidates, gap - candidates[i], path, res, i + 1)
            path.pop()
