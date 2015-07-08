"""Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted. """

# See Interval2 for logic

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if(len(intervals) == 0):
            return intervals
        
        intervals.sort(key = lambda x : x.start)
        result = []
        result.append(intervals[0])
        for i in xrange(len(intervals)):
            current = intervals[i]
            previous = result[-1]
            if(previous.end < current.start):
                result.append(current)
            elif(previous.end < current.end):
                previous.end = current.end
                result.pop()
                result.append(previous)
        return result
        
