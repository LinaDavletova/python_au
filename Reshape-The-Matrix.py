class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        new = []
        newstr = [j for i in nums for j in i]
        if len(newstr) != r * c:
            return nums
        for i in range(r):
            new.append(newstr[i*c:(i+1)*c])
        return new
