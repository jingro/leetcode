class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        a = ['+', '-', '*', '/']
        for i in tokens:
            if i in a:
                v2 = int(nums.pop())
                v1 = int(nums.pop())
                if i == '+':
                    t = v1 + v2
                elif i == '-':
                    t = v1 - v2
                elif i == '*':
                    t = v1 * v2
                else:
                    t = int(1.0 * v1 / v2)
                nums.append(str(t))
            else:
                nums.append(i)
        return int(nums.pop())
