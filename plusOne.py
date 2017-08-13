class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        b = 1
        size = len(digits)
        i = size - 1
        while i >= 0 or b:
            if i < 0:
                digits.insert(0, b)
                break
            a = digits[i]
            sum = a + b
            b = sum / 10
            digits[i] = sum % 10
            i -= 1
        return digits


solution = Solution()
x = [9, 9, 8]
print solution.plusOne(x)
