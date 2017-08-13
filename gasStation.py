class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        t = res = 0
        j = -1
        for i in range(size):
            t += (gas[i] - cost[i])
            res += (gas[i] - cost[i])
            if t < 0:
                t = 0
                j = i
        return j + 1 if res >= 0 else -1
