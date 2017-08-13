class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size < 4:
            return []
        res = []
        d = {}
        for i in range(size - 1):
            for j in range(i + 1, size):
                t = nums[i] + nums[j]
                if t not in d:
                    d[t] = [(i, j)]
                else:
                    d[t].append((i, j))
        for sum in d:
            for i, j in d[sum]:
                if target - sum not in d:
                    continue
                for k, l in d[target - sum]:
                    if i != k and i != l and j != k and j != l:
                        t = [nums[i], nums[j], nums[k], nums[l]]
                        t.sort()
                        res.append(tuple(t))
        return list(set(res))
