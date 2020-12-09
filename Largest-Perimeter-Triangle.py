class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = sorted(A, reverse=True)
        n = len(B)
        i = 0
        while i != n - 2 and B[i] >= B[i + 1] + B[i + 2]:
            i += 1
        if i == n - 2:
            return 0
        return B[i] + B[i + 1] + B[i + 2]
