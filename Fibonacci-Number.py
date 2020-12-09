class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1 or N == 0:
            return N
        prev = 0
        cur = 1
        for i in range(N - 1):
            f = prev + cur
            prev = cur
            cur = f
        return cur
