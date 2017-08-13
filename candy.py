class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        nums = [1 for i in range(size)]
        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
        t = 2
        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                nums[i] = max(nums[i], t)
                t += 1
            else:
                t = 2
        return sum(nums)
