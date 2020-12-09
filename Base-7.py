class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        num7 = 0
        d = 1
        k = 0
        if num < 0:
            k = -1
            num *= -1
        else:
            k = 1
        while num > 0:
            num7 = num7 + num % 7 * d
            num //= 7
            d *= 10
        return str((num7) * k)
