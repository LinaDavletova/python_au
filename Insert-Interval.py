class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)
        intervals.sort(key=lambda elem: (elem[0], elem[1]))
        outint = []
        beginInt = intervals[0][0]
        endInt = intervals[0][1]
        for i in range(1, len(intervals)): 
            if intervals[i][0] <= endInt:
                endInt = max(intervals[i][1], endInt)
            else:
                outint.append([beginInt, endInt])
                beginInt = intervals[i][0]
                endInt = intervals[i][1]
        outint.append([beginInt, endInt])
        return outint
    
