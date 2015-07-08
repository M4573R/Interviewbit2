"""Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] in as [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted."""


""" Analysis : If we sort the list by the interval.start then we can combine all the intervals by a linear traversal.
In the sorted interval if some (i-1)th interval does not overlap with the ith interval, it also does not overlap
with the (i+1)th interval because (i+1)th intervals start value is greater than or equal to ith interval.start.

Implementation : Sort the intervals by their start value. Create empty list/stack. Push the first element into the list.
For each interval i, check if it overlaps with the next one or not. If it does not overlap,push it to the stack. If it does overlap, 
update the i-1th intervals end time with the current intervals end time and push the updated one to the stack
after removing the original. Each (i-1)th and ith interval pair overlaps with one another if the (i-1)th intervals
end value is smaller than the ith one's end value. They do not overlap with one another in the sorted list if the (i-1)th
interval ends before the next one starts i.e (i-1).end < i.start. """


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
    #create empty stack/list
        result = []
        if(len(intervals) == 0):
            return [newInterval]
    #Add the new interval into the given list
        intervals.append(newInterval)
    #Sort the list by the start time of the intervals
        intervals.sort(key = lambda x : x.start)
    #Add the first element to the result list. This would be the stack top
        result.append(intervals[0])
    #For each interval i in intervals see if it overlaps with the previous interval or not. If it does not overlap, 
    # add to result. If it does overlap, then update the previous intervals end time with the current one and add to result.
        for i in xrange(len(intervals)):
    #current and previous stores the ith interval and the (i-1)th interval(which might be merged before)
            current = intervals[i]
            previous = result[-1]
    # if the previous elements end is smaller than the current one's start, it means they don't overlap. Ex : (1,6),(8,10)
            if(previous.end < current.start):
                result.append(current)
    # if the previous elements end is smaller than the current one's start it means they do overlap considering 
    # we already have a sorted list of intervals by their start key. Ex : (1,2),(3,5) should be (1,5)
            elif(previous.end < current.end):
    # if they overlap update the previous intervals end with the current one, pop it to remove the previous one and insert the
    #updated previous. The start time carries over as we are adding the previous one and the current.start gerts merged
                previous.end = current.end
                result.pop()
                result.append(previous)
    # the stack will contain the merged results
        return result
                
                
                
            
         

