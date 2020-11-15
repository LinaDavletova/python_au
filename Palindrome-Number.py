class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = 0
        x1 = x
        while x1 > 0:
            y = 10 * y + x1 % 10
            x1 // = 10
        return y == x
