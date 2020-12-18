class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=0
        n=0
        for i in nums:
            if i==1:
                n+=1
            else:
                if n>num:
                    num=n
                n=0
        if n>num:
                num=n
                n=0
        return num
