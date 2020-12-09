# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
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
```

##Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(intervals) == 0:
        return
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
```

##Insert Interval

https://leetcode.com/problems/insert-interval/

```python
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
```

