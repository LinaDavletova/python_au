class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        y = 0
        if x > 0:
            k = 1
        else:
            k = -1
            x * = -1
        while x > 0:
            y = 10 * y + x % 10
            x // = 10
            if y > 2 ** 31 - 1 or y < -2 ** 31:
                return 0
        return y*k
