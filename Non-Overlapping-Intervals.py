class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda elem: (elem[0], elem[1]))
        kol = 0
        num = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[num][1]:
                num = i      
            else:
                kol += 1
                if intervals[i][1] < intervals[num][1]:
                    num = i
        return kol
